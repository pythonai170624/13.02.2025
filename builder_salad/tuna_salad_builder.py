from typing import override

from salad_builder import SaladBuilder

class TunaSaladBuilder(SaladBuilder):

    @override
    def prepare_vegg(self):
        self.get_salad().prepare_vegg("Tomato and cucumber")

    @override
    def prepare_main(self):
        self.get_salad().prepare_main("Tuna lots of tuna")

    @override
    def prepare_graving(self):
        self.get_salad().prepare_graving("Thousand islands")

    @override
    def prepare_price(self):
        self.get_salad().prepare_price("Today special offer 49.90")
