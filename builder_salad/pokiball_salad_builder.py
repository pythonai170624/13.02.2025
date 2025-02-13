from typing import override

from salad_builder import SaladBuilder

class PokiballSaladBuilder(SaladBuilder):

    def __init__(self):
        super().__init__()

    @override
    def prepare_vegg(self):
        self.get_salad().prepare_vegg("Tomato and cucumber")

    @override
    def prepare_main(self, **kwargs):
        # kwargs == fish type

        self.get_salad().prepare_main(f"lots of {kwargs.get('fish_type', '--missing--')}")

    @override
    def prepare_graving(self):
        self.get_salad().prepare_graving("Thousand islands")

    @override
    def prepare_price(self):
        self.get_salad().prepare_price("Today special offer 49.90")
