from Projects.random_missile_generator.missile_types.tnt_bomb import TNTBomb
from random import randint
from time import sleep


class AntiTNTGun:

    def neutralize(self, missile):
        if isinstance(missile, TNTBomb):
            defence_activation = randint(0, 10)
            if defence_activation % 2 != 0:
                print(f"----------- MISSILE '{missile.serial_number}' DETECTED -----------")
                print(f"- Anti-TNT-Gun DESTROYED MISSILE TNT-Bomb -")
            else:
                print(f"---------- AIR DEFENCE SYSTEM FAILED ----------")
                print(f"-------- Anti-TNT-Gun MISSED TNT-Bomb ---------")
                sleep(1)
                print(f"------- MISSILE '{missile.serial_number}' WAS NOT DESTROYED -------")
