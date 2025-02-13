from abc import ABC, abstractmethod

import pandas as pd

class BaseDataSample (ABC):
    def __init__(self, file_path):
        self.missing_values = None
        self.file_path = file_path
        self.df = None

    def load_data(self):
        self.df = pd.read_csv(self.file_path)

    @abstractmethod
    def calculate_averages(self):
        raise NotImplementedError("This method should be implemented by subclasses")

    @abstractmethod
    def calculate_std_deviation(self):
        raise NotImplementedError("This method should be implemented by subclasses")

    @abstractmethod
    def find_duplicates(self):
        raise NotImplementedError("This method should be implemented by subclasses")

    def calculate_missing_values(self):
        """
        Calculate the number of missing values for each column.
        """
        self.missing_values = self.df.isnull().sum()

    def __str__(self):
        return f"DataFrame (first 5 rows):\n{self.df.head()}"
