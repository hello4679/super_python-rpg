import random
import numpy as np
from character import CHARACTER
import MANAGEMENT
import STATUS


class Enemy(CHARACTER.Character):
    def __init__(self,
                 name='ENEMY',
                 hp=100,
                 mp=100,
                 ap=10,
                 power=100,
                 magic_power=100,
                 spirit_power=100,
                 defence_power=100,
                 luck=10
                 ):
        super().__init__(name, hp, mp, ap, power, magic_power, spirit_power,
                         defence_power, luck)

    def damaged(self):
        if self.hp > self.upper_hp:
            self.hp = self.upper_hp
        if self.mp > self.upper_mp:
            self.mp = self.upper_mp
        if self.ap > self.upper_ap:
            self.ap = self.upper_ap
        s = 0.01 * int(85 * (1 + (self.luck * 0.001)))
        if s < 1:
            m = 1 - s
        else:
            m = 0
        judge = np.random.choice(['success', 'failure'], p=[s, m])
        if judge == 'success':
            MANAGEMENT.total_damage = int((MANAGEMENT.physical_damage
                                           * (1-(self.defence_power/1000)))
                                          + MANAGEMENT.magic_damage
                                          * ((1-(self.defence_power/1000))
                                             * (1-(self.spirit_power/1000))))
            print(MANAGEMENT.physical_damage)
            print(MANAGEMENT.magic_damage)
            print(MANAGEMENT.total_damage)

            if MANAGEMENT.total_damage <= 0:
                MANAGEMENT.total_damage = 0
            self.hp -= MANAGEMENT.total_damage
            self.limit_count += MANAGEMENT.total_damage
            print(f'{self.name}に{MANAGEMENT.total_damage}ダメージ！！')
        else:
            print(f'{self.name}はひらりと躱した！！')
        if MANAGEMENT.total_damage > 0:
            MANAGEMENT.total_damage = 0
        MANAGEMENT.physical_damage = 0
        MANAGEMENT.magic_damage = 0

    def enemy_attack(self):
        print(f'>{self.name}の攻撃')
        harf_power = int(self.power * 0.5)
        MANAGEMENT.enemy_physical_damage = int(
            random.uniform(harf_power, self.power))

    def enemy_magic_1(self):
        cost_mp = STATUS.MP_3
        if self.mp >= cost_mp:
            print(f'>>{self.name}は魔法を唱えた')
            self.mp -= cost_mp
            harf_magic_power = int(self.magic_power * 0.5)
            MANAGEMENT.enemy_magic_damage = int(
                random.uniform(harf_magic_power, self.magic_power))
        else:
            print(f'>{self.name}はMPが足りない！！')

    def enemy_action(self):
        anum = random.random()
        if anum >= 0.5:
            self.enemy_attack()
        else:
            self.enemy_magic_1()
