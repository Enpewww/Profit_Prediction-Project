import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin

class DateExtractor(BaseEstimator, TransformerMixin):
    def __init__(self, date_column='Order_Date'):
        self.date_column = date_column

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X = X.copy()

        # Check if column exists
        if self.date_column not in X.columns:
            raise ValueError(f"Missing column: '{self.date_column}' required to input the date data.")

        # Convert to datetime
        X[self.date_column] = pd.to_datetime(X[self.date_column], errors='coerce')

        # Check for missing or invalid dates (incase)
        if X[self.date_column].isnull().any():
            raise ValueError(f"Missing or invalid values found in '{self.date_column}'. Please provide any complete date.")

        # Feature Creation
        X['Order_Year'] = X[self.date_column].dt.year.astype('object')
        X['Order_Month'] = X[self.date_column].dt.month.astype('object')
        X['Order_DayOfWeek'] = X[self.date_column].dt.dayofweek.astype('object')

        # Drop the Order_Date Column
        return X.drop(columns=[self.date_column])