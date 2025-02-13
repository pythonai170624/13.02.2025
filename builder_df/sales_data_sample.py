from base_data_sample import BaseDataSample

class SalesDataSample(BaseDataSample):
    def __init__(self, file_path):
        super().__init__(file_path)
        self.duplicates = None
        self.std_by_region = None

    def calculate_averages(self):
        """
        Calculate the average sales per quantity.
        """
        self.df["SalesPerUnit"] = self.df["Sales"] / self.df["Quantity"]

    def calculate_std_deviation(self):
        """
        Calculate the standard deviation of sales by region.
        """
        self.std_by_region = self.df.groupby("Region")["Sales"].std()

    def find_duplicates(self):
        """
        Find duplicate products (based on Product and Region).
        """
        self.duplicates = self.df[self.df.duplicated(subset=["Product", "Region"])]
