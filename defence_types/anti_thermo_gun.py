from Projects.random_missile_generator.missile_types.thermo_nuclear import ThermoNuclear
from random import randint
from time import sleep


class AntiThermoGun:

    def neutralize(self, missile):
        if isinstance(missile, ThermoNuclear):
            defence_activation = randint(0, 10)
            if defence_activation % 2 != 0:
                print(f"---------- MISSILE '{missile.serial_number}' DETECTED ----------")
                print(f"- Anti-Thermo-Gun DESTROYED MISSILE Facet-Bomb -")
            else:
                print(f"----------- AIR DEFENCE SYSTEM FAILED ----------")
                print(f"---- Anti-Thermo-Gun MISSED Thermo-Nuclear -----")
                sleep(1)
                print(f"------- MISSILE '{missile.serial_number}' WAS NOT DESTROYED -------")
