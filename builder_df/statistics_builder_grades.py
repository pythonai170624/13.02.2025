from statistics_builder_abstract import AbstractStatisticsBuilder

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
        self.data_sample.df["Average"] = self.data_sample.df.iloc[:, 1:].mean(axis=1)

    def add_std_deviation(self):
        """
        Add standard deviation for grades.
        """
        self.data_sample.df["StdDev"] = self.data_sample.df.iloc[:, 1:].std(axis=1)

    def add_duplicates(self):
        """
        Identify duplicate rows in the grades data.
        """
        self.data_sample.set_duplicates(self.data_sample.df[self.data_sample.df.duplicated()])

    def add_missing_values(self):
        """
        Calculate missing values in the grades data.
        """
        self.data_sample.missing_values = self.data_sample.df.isnull().sum()
