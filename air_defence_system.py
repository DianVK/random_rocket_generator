from Projects.random_missile_generator.defence_types.anti_facet_gun import AntiFacetGun
from Projects.random_missile_generator.defence_types.anti_thermo_gun import AntiThermoGun
from Projects.random_missile_generator.defence_types.anti_tnt_gun import AntiTNTGun


class AirDefenceSystem:
    def __init__(self):
        self.anti_thermo_gun = AntiThermoGun()
        self.anti_facet_gun = AntiFacetGun()
        self.anti_tnt_gun = AntiTNTGun()

    def intercept_missile(self, missile):
        if missile.missile_type == "ThermoNuclear":
            self.anti_thermo_gun.neutralize(missile)
        elif missile.missile_type == "FacetBomb":
            self.anti_facet_gun.neutralize(missile)
        elif missile.missile_type == "AntiTNTGun":
            self.anti_tnt_gun.neutralize(missile)