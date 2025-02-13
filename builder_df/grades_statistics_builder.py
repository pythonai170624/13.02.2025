from abstract_statistics_builder import AbstractStatisticsBuilder
from grades_data_sample import GradesDataSample

class GradesStatisticsBuilder(AbstractStatisticsBuilder):
    def load_data(self):
        """
        Load grades data from the CSV file.
        """
        self.data_sample.load_data()

    def add_averages(self):
        """
        Add averages for grades.
        """
        self.data_sample.calculate_averages()

    def add_std_deviation(self):
        """
        Add standard deviation for grades.
        """
        self.data_sample.calculate_std_deviation()

    def add_duplicates(self):
        """
        Identify duplicate rows in the grades data.
        """
        self.data_sample.find_duplicates()

    def add_missing_values(self):
        """
        Calculate missing values in the grades data.
        """
        self.data_sample.calculate_missing_values()
