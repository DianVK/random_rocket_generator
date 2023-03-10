import time
from Projects.random_missile_generator.generator import generate_random_missile
from Projects.random_missile_generator.air_defence_system import AirDefenceSystem

print("---------------- CHOOSE OPTION ---------------- ")
print("---------- OPTION - 1 - INDEFINITELY ---------- ")
print("---------- OPTION - 2 - FIXED NUMBER ---------- ")
choose_option = int(input("INPUT OPTION NUMBER : "))
if choose_option == 1:
    while True:
        missile = generate_random_missile()
        air_defence_system = AirDefenceSystem()
        print("------------------------------------------------- ")
        print("---------------- !!! WARNING !!! ---------------- ")
        time.sleep(1)
        print("-----------!!! LAUNCHING MISSILE !!!-------------")
        time.sleep(1)
        print("----------------------- 3 -----------------------")
        time.sleep(1)
        print("----------------------- 2 -----------------------")
        time.sleep(1)
        print("----------------------- 1 -----------------------")
        time.sleep(1)
        print("------- MISSILE TYPE ------ SERIAL NUMBER -------")
        print(f"------- '{missile.missile_type}' -------- '{missile.serial_number}' -----------")
        time.sleep(3)
        print("------------------------------------------------- ")
        print("-------- ACTIVATING AIR DEFENCE SYSTEM  ---------")
        print("------------------------------------------------- ")
        time.sleep(2)
        air_defence_system.intercept_missile(missile)
        time.sleep(4)

elif choose_option == 2:
    option_2 = int(input("Choose number greater than 10: "))
    while option_2 <= 10:
        option_2 = int(input("Invalid number! Choose number greater than 10: "))
    for _ in range(0, option_2):
        missile = generate_random_missile()
        air_defence_system = AirDefenceSystem()
        print("------------------------------------------------- ")
        print("---------------- !!! WARNING !!! ---------------- ")
        time.sleep(1)
        print("-----------!!! LAUNCHING MISSILE !!!-------------")
        time.sleep(1)
        print("----------------------- 3 -----------------------")
        time.sleep(1)
        print("----------------------- 2 -----------------------")
        time.sleep(1)
        print("----------------------- 1 -----------------------")
        time.sleep(1)
        print("------- MISSILE TYPE ------ SERIAL NUMBER -------")
        print(f"------- '{missile.missile_type}' -------- '{missile.serial_number}' -----------")
        time.sleep(3)
        print("------------------------------------------------- ")
        print("-------- ACTIVATING AIR DEFENCE SYSTEM  ---------")
        print("------------------------------------------------- ")
        time.sleep(2)
        air_defence_system.intercept_missile(missile)
        time.sleep(4)
