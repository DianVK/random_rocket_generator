from Projects.random_missile_generator.missile_types.facet_bomb import FacetBomb


class AntiFacetGun:

    def neutralize(self, missile):
        if isinstance(missile, FacetBomb):
            print(f"--- Anti-Facet-Gun DESTROYED MISSILE {missile.serial_number} ---")
        else:
            print("Anti-Facet-System cannot neutralize missile with serial number", missile.serial_number)