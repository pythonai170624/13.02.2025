from base_data_sample import BaseDataSample

class GradesDataSample(BaseDataSample):
    def __init__(self, file_path):
        super().__init__(file_path)
        self.duplicates = None

    def calculate_averages(self):
        """
        Calculate the average grade for each student.
        """
        self.df["Average"] = self.df.iloc[:, 1:].mean(axis=1)

    def calculate_std_deviation(self):
        """
        Calculate the standard deviation of grades for each student.
        """
        self.df["StdDev"] = self.df.iloc[:, 1:].std(axis=1)

    def find_duplicates(self):
        """
        Find duplicate students (based on all columns).
        """
        self.duplicates = self.df[self.df.duplicated()]
