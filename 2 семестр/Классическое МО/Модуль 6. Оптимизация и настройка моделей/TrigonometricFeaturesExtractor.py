from sklearn.base import BaseEstimator, TransformerMixin
import numpy as np
import math

class TrigonometricFeaturesExtractor(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        self.is_fitted_ = True
        return self

    def transform(self, X):
        X_copy = X.copy()
        # Добавляем тригонометрические признаки для временных признаков
        X_copy['sin_month'] = X_copy['month'].apply(math.sin)
        X_copy['cos_month'] = X_copy['month'].apply(math.cos)

        X_copy['sin_hour'] = X_copy['hour'].apply(math.sin)
        X_copy['cos_hour'] = X_copy['hour'].apply(math.cos)

        X_copy['hour_sin'] = (X_copy['hour'] / 23 * 2 * np.pi).apply(math.sin)
        X_copy['hour_cos'] = (X_copy['hour'] / 23 * 2 * np.pi).apply(math.cos)

        X_copy['month_sin'] = ((X_copy['month'] - 1) / 11 * 2 * np.pi).apply(math.sin)
        X_copy['month_cos'] = ((X_copy['month'] - 1) / 11 * 2 * np.pi).apply(math.cos)

        # Преобразуем дату в индекс, если нужно для дальнейшего использования
        day = 24
        year = 365.2425 * day

        X_copy['day_sin'] = (X_copy['hour'] * 2 * np.pi / day).apply(math.sin)
        X_copy['day_cos'] = (X_copy['hour'] * 2 * np.pi / day).apply(math.cos)

        X_copy['year_sin'] = (X_copy['hour'] * 2 * np.pi / year).apply(math.sin)
        X_copy['year_cos'] = (X_copy['hour'] * 2 * np.pi / year).apply(math.cos)

        return X_copy