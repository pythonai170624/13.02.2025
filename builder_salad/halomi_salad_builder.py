from typing import override

from salad_builder import SaladBuilder

class HalomiSaladBuilder(SaladBuilder):
    @override
    def prepare_vegg(self):
        self.get_salad().prepare_vegg("lettuce and carrot")

    @override
    def prepare_main(self):
        self.get_salad().prepare_main("Halomi 500 gram")

    @override
    def prepare_graving(self):
        self.get_salad().prepare_graving("mayo")

    @override
    def prepare_price(self):
        self.get_salad().prepare_price("Today special offer 59.90")
