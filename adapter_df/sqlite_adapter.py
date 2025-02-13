import pandas as pd
from df_statistics import DataFrameStatistics

class AdapterSQLitetoDF:
    def __init__(self, sqlite_result):
        self.sqlite_result = sqlite_result

    def calculate_averages(self):
        # adaptee
        df = pd.DataFrame(self.sqlite_result)

        # calling the good api
        df_statistics = DataFrameStatistics(df)
        result = df_statistics.calculate_averages()

        return  result

    def calculate_std_deviation(self):
        df_statistics = DataFrameStatistics(pd.DataFrame(self.sqlite_result))
        return df_statistics.calculate_std_deviation()

    def find_duplicates(self):
        df_statistics = DataFrameStatistics(pd.DataFrame(self.sqlite_result))
        return df_statistics.find_duplicates()

    def calculate_missing_values(self):
        df_statistics = DataFrameStatistics(pd.DataFrame(self.sqlite_result))
        return df_statistics.calculate_missing_values()
