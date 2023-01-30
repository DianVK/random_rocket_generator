import time
import random
from Projects.random_missile_generator.generator import generate_random_missile
from Projects.random_missile_generator.air_defence_system import AirDefenceSystem


choose_option = int(input("Choose option, 1 for indefinitely or 2 for fixed number: "))
if choose_option == 1:
    while True:
        missile = generate_random_missile()
        air_defence_system = AirDefenceSystem()
        print("---------------- !!! WARNING !!! ----------------- ")
        time.sleep(1)
        print("-----------!!! LAUNCHING MISSILE !!!--------------")
        time.sleep(1)
        print("----------------------- 3 -----------------------")
        time.sleep(1)
        print("----------------------- 2 -----------------------")
        time.sleep(1)
        print("----------------------- 1 -----------------------")
        time.sleep(1)
        print("------- MISSILE TYPE ------ SERIAL NUMBER ------")
        print(f"------- '{missile.missile_type}' -------- '{missile.serial_number}' -------")
        time.sleep(3)
        print("-------- ACTIVATING AIR DEFENCE SYSTEM  --------")
        defence_activation = random.choice(["YES", "NO"])
        if defence_activation == "YES":
            air_defence_system.intercept_missile(missile)
        elif defence_activation == "NO":
            print(f"-------- AIR DEFENCE SYSTEM FAILED --------")
            time.sleep(2)
            print(f"-------- MISSILE WAS NOT DESTROYED --------")
        time.sleep(3)

elif choose_option == 2:
    option_2 = int(input("Choose number greater than 10: "))
    while option_2 <= 10:
        option_2 = int(input("Invalid number! Choose number greater than 10: "))
    for _ in range(0, option_2):
        missile = generate_random_missile()
        air_defence_system = AirDefenceSystem()
        print("!!! WARNING !!! ")
        print(f"Missile type '{missile.missile_type}' with serial number '{missile.serial_number}' was Launched!")
        defence_activate = random.randint(0,100)
        if defence_activate % 2 != 0:
            time.sleep(1)
            air_defence_system.intercept_missile(missile)
        time.sleep(3)