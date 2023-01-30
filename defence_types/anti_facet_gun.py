from Projects.random_missile_generator.missile_types.facet_bomb import FacetBomb
from random import randint
from time import sleep


class AntiFacetGun:

    def neutralize(self, missile):
        if isinstance(missile, FacetBomb):
            defence_activation = randint(0, 10)
            if defence_activation % 2 != 0:
                print(f"----------- MISSILE '{missile.serial_number}' DETECTED -----------")
                print(f"- Anti-Facet-Gun DESTROYED MISSILE Facet-Bomb -")
            else:
                print(f"----------- AIR DEFENCE SYSTEM FAILED -----------")
                print(f"------- Anti-Facet-Gun MISSED Facet-Bomb --------")
                sleep(1)
                print(f"------- MISSILE '{missile.serial_number}' WAS NOT DESTROYED -------")
