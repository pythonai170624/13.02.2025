import pandas as pd
from abstract_statistics import AbstractStatistics

class DataFrameStatistics(AbstractStatistics):
    def __init__(self, df):
        self.df = df

    def calculate_averages(self):
        return self.df.mean(numeric_only=True)

    def calculate_std_deviation(self):
        return self.df.std(numeric_only=True)

    def find_duplicates(self):
        return self.df[self.df.duplicated()]

    def calculate_missing_values(self):
        return self.df.isnull().sum()
