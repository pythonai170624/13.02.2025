from abc import abstractmethod, ABC
from typing import final

from salad import Salad

class SaladBuilder(ABC):
    def __init__(self):
        self.__salad: Salad = None

    def get_salad(self):
        return self.__salad

    @final
    def build_salad(self):
        self.__salad = Salad()  # 1
        self.prepare_vegg()  # 2
        self.prepare_main()  # 3
        self.prepare_graving()  # 4
        self.prepare_price()  # 5
        return self

    @abstractmethod
    def prepare_vegg(self):
        raise NotImplementedError

    @abstractmethod
    def prepare_main(self):
        raise NotImplementedError

    @abstractmethod
    def prepare_graving(self):
        raise NotImplementedError

    @abstractmethod
    def prepare_price(self):
        raise NotImplementedError
