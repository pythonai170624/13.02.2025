from statistics_builder_abstract import AbstractStatisticsBuilder

class SalesStatisticsBuilder(AbstractStatisticsBuilder):
    def load_data(self):
        """
        Load grades data from the CSV file.
        """
        self.data_sample.load_data()

    def add_averages(self):
        """
        Add averages for grades.
        """
        df = self.data_sample.df
        df["SalesPerUnit"] = df["Sales"] / df["Quantity"]

    def add_std_deviation(self):
        """
        Add standard deviation for grades.
        """
        self.data_sample.std_by_region = self.data_sample.df.groupby("Region")["Sales"].std()


    def add_duplicates(self):
        """
        Identify duplicate rows in the grades data.
        """
        self.data_sample.set_duplicates(
            self.data_sample.df[self.data_sample.df.duplicated(subset=["Product", "Region"])])

    def add_missing_values(self):
        """
        Calculate missing values in the grades data.
        """
        self.data_sample.missing_values = self.data_sample.df.isnull().sum()
