from builder_salad.halomi_salad_builder import HalomiSaladBuilder
from builder_salad.pokiball_salad_builder import PokiballSaladBuilder
from builder_salad.salad import Salad
from tuna_salad_builder import TunaSaladBuilder

if __name__ == "__main__":
    tuna_salad: Salad = TunaSaladBuilder().build_salad().get_salad()
    print(tuna_salad)

    halomi_salad: Salad = HalomiSaladBuilder().build_salad().get_salad()
    print(halomi_salad)

    poki_ball_salad = PokiballSaladBuilder().build_salad().get_salad()
    print(poki_ball_salad)
