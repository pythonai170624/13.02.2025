from abc import ABC, abstractmethod

from builder_df.data_sample import DataSample


class AbstractStatisticsBuilder(ABC):
    def __init__(self, file_path):
        self.data_sample = DataSample(file_path)

    @abstractmethod
    def load_data(self):
        """
        Step 1: Load data from the file.
        """
        pass

    @abstractmethod
    def add_averages(self):
        """
        Step 2: Calculate averages.
        """
        pass

    @abstractmethod
    def add_std_deviation(self):
        """
        Step 3: Calculate standard deviation.
        """
        pass

    @abstractmethod
    def add_duplicates(self):
        """
        Step 4: Identify duplicates.
        """
        pass

    @abstractmethod
    def add_missing_values(self):
        """
        Step 5: Calculate missing values.
        """
        pass

    def build(self):
        """
        Orchestrate all steps to build the data sample.
        """
        self.load_data()
        self.add_averages()
        self.add_std_deviation()
        self.add_duplicates()
        self.add_missing_values()
        return self.data_sample
