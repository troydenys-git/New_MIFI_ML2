from sklearn.base import BaseEstimator, TransformerMixin
import numpy as np
import math

class TimeFeaturesExtractor(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        self.is_fitted_ = True
        return self  # Мы не нуждаемся в обучении для этой трансформации

    def transform(self, X):
        X_copy = X.copy()
        # Извлекаем временные признаки
        X_copy['year'] = X_copy['datetime'].dt.year
        X_copy['month'] = X_copy['datetime'].dt.month
        X_copy['season'] = X_copy['datetime'].dt.quarter
        X_copy['day'] = X_copy['datetime'].dt.day
        X_copy['hour'] = X_copy['datetime'].dt.hour
        X_copy['dayofyear'] = X_copy['datetime'].dt.dayofyear # В новых версиях pandas без нижнего подчеркивания
        X_copy['dayofweek'] = X_copy['datetime'].dt.dayofweek
        X_copy['is_weekend'] = X_copy['dayofweek'].isin([5, 6]).astype(int)

        # Убираем колонку 'datetime' после обработки
        X_copy = X_copy.drop(columns=['datetime'])

        return X_copy