from builder_salad.halomi_salad_builder import HalomiSaladBuilder
from tuna_salad_builder import TunaSaladBuilder

if __name__ == "__main__":
    tuna_salad = TunaSaladBuilder().build_salad().get_salad()
    print(tuna_salad)

    halomi_salad = HalomiSaladBuilder().build_salad().get_salad()
    print(halomi_salad)
