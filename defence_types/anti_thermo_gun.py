from Projects.random_missile_generator.missile_types.thermo_nuclear import ThermoNuclear


class AntiThermoGun:

    def neutralize(self, missile):
        if isinstance(missile, ThermoNuclear):
            print(f"--- Anti-Thermo-Gun DESTROYED MISSILE {missile.serial_number} ---")

        else:
            print("Anti-Thermo-System cannot neutralize missile with serial number", missile.serial_number)