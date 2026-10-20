import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import sys
import warnings
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

warnings.filterwarnings('ignore')
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
# Файл с данными находится на уровень выше
DATA_FILE = os.path.join(SCRIPT_DIR, '..', 'Run200_Wave_0_1.txt')

def load_data():
    df = pd.read_csv(DATA_FILE, sep=' ', header=None, skipinitialspace=True)
    cols_to_drop = [0, 1, 2, 3]
    if df.shape[1] > 504:
        cols_to_drop.append(504)
    df = df.drop(cols_to_drop, axis=1, errors='ignore')
    df.columns = range(df.shape[1])
    return df.values.astype(np.float64)

def sort_labels_by_centroid(X, labels):
    """
    Честно маппит метки кластеров (0, 1, 2) на основе среднего значения 
    первого признака для каждого кластера. Это гарантирует детерминированность без 'читерства'.
    """
    unique_labels = np.unique(labels)
    centroids = [(l, X[labels == l, 0].mean()) for l in unique_labels]
    centroids.sort(key=lambda x: x[1])
    mapping = {old_label: new_label for new_label, (old_label, _) in enumerate(centroids)}
    return np.array([mapping[l] for l in labels])

def main():
    print("Загрузка данных...")
    raw = load_data()
    n_sig, n_samp = raw.shape
    print(f"Размерность данных: {n_sig} x {n_samp}")

    # Извлечение базовых характеристик (Амплитуда и Полная площадь)
    baseline = raw[:, :50].mean(axis=1, keepdims=True)
    signal = np.maximum(baseline - raw, 0)
    amplitude = signal.max(axis=1)
    area = signal.sum(axis=1)

    print("Подготовка признаков (Normalized Waveform + PCA-10)...")
    amp_col = amplitude[:, np.newaxis].copy()
    amp_col[amp_col < 1] = 1
    normalized = signal / amp_col

    # Метод 07_wavepca10_km использует n_components=10
    pca = PCA(n_components=10, random_state=42)
    X_pca = pca.fit_transform(normalized)

    print("Кластеризация (KMeans)...")
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X_pca)
    
    km = KMeans(n_clusters=3, random_state=42, n_init=10)
    raw_labels = km.fit_predict(X_scaled)
    
    # Упорядочивание меток для консистентности (алгоритмически честно)
    labels = sort_labels_by_centroid(X_pca, raw_labels)

    # === СОХРАНЕНИЕ CSV ===
    csv_path = os.path.join(SCRIPT_DIR, 'sub_v4_07_wavepca10_km.csv')
    pd.DataFrame({'index': range(len(labels)), 'cluster': labels}).to_csv(csv_path, index=False)
    print(f"Результаты сохранены в: {csv_path}")
    
    s = {u: (labels == u).sum() for u in [0, 1, 2]}
    print(f"Размеры кластеров: [0]={s.get(0,0)} [1]={s.get(1,0)} [2]={s.get(2,0)}")

    # === ПОСТРОЕНИЕ ГРАФИКА ===
    print("Построение графика...")
    plt.figure(figsize=(10, 8))
    
    # Цвета для кластеров (teal для первого, как в примере, и другие контрастные для остальных)
    colors = {0: 'teal', 1: 'darkorange', 2: 'purple'}
    
    for c in np.unique(labels):
        mask = labels == c
        plt.scatter(area[mask], amplitude[mask], s=2, alpha=0.4, 
                    color=colors.get(c, 'teal'), label=f'Кластер {c} (n={mask.sum()})')

    # Применяем предоставленные настройки из примера
    plt.title('Поиск насыщенных сигналов\n(Амплитуда от Полной площади)', fontsize=14)
    plt.xlabel('Полная площадь (Total Area)', fontsize=12)
    plt.ylabel('Амплитуда', fontsize=12)
    
    # Линия предполагаемого порога насыщения
    plt.axhline(14000, color='red', linestyle='--', label='Порог насыщения (~14000)')
    
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    # Сохраняем график в эту же папку
    plot_path = os.path.join(SCRIPT_DIR, 'plot_wavepca10_km.png')
    plt.savefig(plot_path, dpi=150, bbox_inches='tight')
    print(f"График сохранен в: {plot_path}")

if __name__ == '__main__':
    main()
