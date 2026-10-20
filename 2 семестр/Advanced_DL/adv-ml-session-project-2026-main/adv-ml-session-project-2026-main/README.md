# Классификация музыкальных жанров: MLP vs CNN vs EfficientNet

Сравнение трёх подходов к классификации спектрограмм GTZAN: полносвязная сеть (MLP из референса), собственная свёрточная сеть (CNN) и transfer learning на EfficientNet B0.

## Структура проекта

| Файл | Описание |
|------|----------|
| `main.ipynb` | Решение задания: CNN, EfficientNet, таблица сравнения и выводы |
| `reference.ipynb` | Референс из курса |
| `download_dataset.py` | Скрипт загрузки датасета с Kaggle |
| `justfile` | Команды для окружения, загрузки данных и запуска ноутбука |

## Требования

- Python 3.12
- uv
- Токен Kaggle API для скачивания датасета

## Быстрый старт

```bash
# 1. Клонировать репозиторий и перейти в папку проекта
cd adv-ml

# 2. Установить зависимости
just install

# 3. Настроить Kaggle API
cp .env.example .env
# Вписать KAGGLE_API_TOKEN=... (https://www.kaggle.com/settings → Create New Token)

# 4. Скачать датасет
just download-dataset

# 5. Открыть ноутбук
just notebook
```

Выполнить все ячейки `main.ipynb` сверху вниз.

### Запуск без UI

```bash
just execute
```

## Датасет

[GTZAN Music Genre Classification](https://www.kaggle.com/datasets/andradaolteanu/)

## Что реализовано в main.ipynb

### CNN

- 3 свёрточных слоя: 32 → 64 → 128 каналов
- После каждого: ReLU + MaxPooling
- Полносвязный блок: 256 нейронов (ReLU) → Dropout(0.3) → 10 классов
- Вход 128×128, AdamW, 50 эпох

### Transfer Learning (EfficientNet B0)

- Предобученные веса ImageNet, все слои заморожены
- Классификатор заменён на 10 классов
- Аугментация: RandomHorizontalFlip, RandomRotation
- Вход 224×224, Adam, 30 эпох

## Переменные окружения

| Переменная | Описание |
|------------|----------|
| `KAGGLE_API_TOKEN` | Токен Kaggle (файл `.env` или `~/.kaggle/kaggle.json`) |
