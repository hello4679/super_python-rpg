
class Character(object):
    def __init__(self,
                 name,
                 hp,
                 mp,
                 ap,
                 power,
                 magic_power,
                 spirit_power,
                 defence_power,
                 luck
                 ):
        self.name = name
        self.hp = hp * (1 + int(
            (power * 0.02) * (spirit_power * 0.02)))
        self.mp = mp * (1 + int(
            (magic_power * 0.01) * (spirit_power * 0.01)))
        self.ap = ap
        self.power = power
        self.magic_power = magic_power
        self.spirit_power = spirit_power
        self.defence_power = defence_power
        self.luck = luck
        self.upper_hp = self.hp
        self.upper_mp = self.mp
        self.upper_ap = self.ap
        self.limit_count = 0
        self.gauge_count = 0
        self.gauge = '         '
