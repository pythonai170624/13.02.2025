from abc import ABC, abstractmethod

class AbstractStatistics(ABC):
    @abstractmethod
    def calculate_averages(self):
        pass

    @abstractmethod
    def calculate_std_deviation(self):
        pass

    @abstractmethod
    def find_duplicates(self):
        pass

    @abstractmethod
    def calculate_missing_values(self):
        pass
