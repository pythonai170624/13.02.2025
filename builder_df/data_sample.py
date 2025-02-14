import pandas as pd

class DataSample:
    def __init__(self, file_path):
        self.missing_values = None
        self.file_path = file_path
        self.df = None
        self.duplicates = None

    def load_data(self):
        self.df = pd.read_csv(self.file_path)

    def set_duplicates(self, dup):
        """
        Find duplicate students (based on all columns).
        """
        self.duplicates = dup

    def set_missing_values(self, miss):
        """
        Calculate the number of missing values for each column.
        """
        self.missing_values = miss

    def __str__(self):
        return f"DataFrame (first 5 rows):\n{self.df.head()}"
