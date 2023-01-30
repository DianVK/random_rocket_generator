from Projects.random_missile_generator.air_defence_system import AirDefenceSystem


class AntiFacetGun(AirDefenceSystem):

    def __init__(self,serial_num):
        super().__init__(serial_num,"AntiFacetGun")