from Projects.random_missile_generator.random_missile_generator import RandomMissileGenerator


class FacetBomb(RandomMissileGenerator):
    def __init__(self,serial_number):
        super().__init__(serial_number,"Facet-Bomb")
