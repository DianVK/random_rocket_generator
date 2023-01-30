from Projects.randommissilegenerator.main import RandomMissileGenerator


class ThermoNuclear(RandomMissileGenerator):
    def __init__(self,serial_number):
        super().__init__(serial_number,"ThermoNuclear")
