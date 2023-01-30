from Projects.random_missile_generator.missile_types.tnt_bomb import TNTBomb


class AntiTNTGun:

    def neutralize(self, missile):
        if isinstance(missile, TNTBomb):
            print(f"--- Anti-TNT-Gun DESTROYED MISSILE {missile.serial_number} ---")
        else:
            print("Anti-TNT-System cannot neutralize missile with serial number", missile.serial_number)