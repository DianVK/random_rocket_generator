import time
from Projects.random_missile_generator.generator import generate_random_missile


choose_option = int(input("Choose option, 1 for indefinitely or 2 for fixed number: "))
if choose_option == 1:
    while True:
        missile = generate_random_missile()
        print(f"Missile type '{missile.missile_type}' with serial number '{missile.serial_number}'was generated!")
        time.sleep(3)
elif choose_option == 2:
    option_2 = int(input("Choose number greater than 10: "))
    for _ in range(0, option_2):
        missile = generate_random_missile()
        print(f"Missile type '{missile.missile_type}' was generated!")
        time.sleep(3)