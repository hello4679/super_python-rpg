from character import PLAYER
import MANAGEMENT
import random
import STATUS
from template import UI
import numpy as np


class Knight(PLAYER.Player):
    def __init__(self,
                 name='みならいナイト',
                 hp=100,
                 mp=100,
                 ap=100,
                 power=150,
                 magic_power=100,
                 spirit_power=125,
                 defence_power=150,
                 luck=10
                 ):
        super().__init__(name, hp, mp, ap, power, magic_power, spirit_power,
                         defence_power, luck)
        self.COMMAND = '  SELECT COMMAND '

    def limit_break_1(self):
        if self.gauge_count >= 1:
            print(r'>\ \ \ 暗黒剣 / / /')
            MANAGEMENT.physical_damage = int(self.power * 15)
            self.hp -= 250
            self.limit_count = 0
        else:
            print('>リミットゲージが足りません')
            self.select_limit()

    def limit_break_2(self):
        if self.gauge_count >= 2:
            print(r'>\ \ \ ヒョック / / /')
            MANAGEMENT.magic_damage = int(self.hp * self.luck)
            self.limit_count = 0
        else:
            print('>リミットゲージが足りません')
            self.select_limit()

    def limit_break_3(self):
        if self.gauge_count >= 3:
            print(r'>\ \ \ 連続剣 / / /')
            for i in range(10):
                MANAGEMENT.magic_damage += int(self.power ** 0.5)
                print(f'{MANAGEMENT.magic_damage}!!')
            self.limit_count = 0
        else:
            print('>リミットゲージが足りません')
            self.select_limit()

    def limit_break_4(self):
        if self.gauge_count >= 4:
            print(r'>\ \ \ NONE / / /')
            self.limit_count = 0
        else:
            print('>リミットゲージが足りません')
            self.select_limit()

    def job_action_1(self):
        cost_ap = STATUS.AP_3
        if self.ap >= cost_ap:
            print(f'>{self.name}のざんげき')
            self.ap -= cost_ap
            times_power = int(self.power * 2)
            MANAGEMENT.physical_damage = int(
                random.uniform(self.power, times_power))
        else:
            print('>APが足りない！！')
            self.select_job_action()

    def job_action_2(self):
        cost_ap = STATUS.AP_3
        if self.ap >= cost_ap:
            print(f'>{self.name}のとつげき')
            self.ap -= cost_ap
            times_power = int(self.power * 2)
            harf_power = int(self.power * 0.1)
            MANAGEMENT.physical_damage = int(
                random.uniform(harf_power, times_power))
        else:
            print('>APが足りない！！')
            self.select_job_action()

    def job_action_3(self):
        cost_ap = STATUS.AP_3
        if self.ap >= cost_ap:
            print(f'>{self.name}のサガク剣')
            self.ap -= cost_ap
            MANAGEMENT.physical_damage = self.upper_hp - self.hp
        else:
            print('>APが足りない！！')
            self.select_job_action()

    def job_action_4(self):
        cost_ap = STATUS.AP_3
        if self.ap >= cost_ap:
            print(f'>{self.name}のひあひぬき')
            self.ap -= cost_ap
            at = np.random.choice(['success', 'failure'], p=[0.05, 0.95])
            if at == 'success':
                MANAGEMENT.physical_damage = 999
            else:
                print('...')
        else:
            print('>APが足りない！！')
            self.select_job_action()

    def select_job_action(self):
        self.limit_gauge(self.limit_count)
        self.show_limit()
        action_contents = UI.BATTLE_UI.substitute(sec1='ざんげき ',
                                                  sec2='とつげき ',
                                                  sec3='サガク剣 ',
                                                  sec4='ひあひぬき',
                                                  sec5=STATUS.AP_3,
                                                  sec6=STATUS.AP_3,
                                                  sec7=STATUS.AP_3,
                                                  sec8=STATUS.AP_3,
                                                  sec9=self.name,
                                                  sec10=self.hp,
                                                  sec11=self.upper_hp,
                                                  sec12=self.mp,
                                                  sec13=self.upper_mp,
                                                  sec14=self.gauge,
                                                  sec15=self.ap,
                                                  sec16=self.upper_ap,
                                                  sec98=self.COMMAND,
                                                  sec99=MANAGEMENT.TURN
                                                  )
        print(action_contents)
        try:
            a = int(input('セレクトコマンド>>>'))
            if a == 1:
                self.job_action_1()
            elif a == 2:
                self.job_action_2()
            elif a == 3:
                self.job_action_3()
            elif a == 4:
                self.job_action_4()
            elif a == 5:
                self.select_command()
            elif a == 6:
                self.select_limit()
        except IndexError:
            print('無効な入力です。')
            self.select_command()

    def select_limit(self):
        self.limit_gauge(self.limit_count)
        self.show_limit()
        action_contents = UI.BATTLE_UI.substitute(sec1='暗黒剣？',
                                                  sec2='ヒョック',
                                                  sec3='連続剣　',
                                                  sec4='　　　　',
                                                  sec5='1',
                                                  sec6='2',
                                                  sec7='3',
                                                  sec8='4',
                                                  sec9=self.name,
                                                  sec10=self.hp,
                                                  sec11=self.upper_hp,
                                                  sec12=self.mp,
                                                  sec13=self.upper_mp,
                                                  sec14=self.gauge,
                                                  sec15=self.ap,
                                                  sec16=self.upper_ap,
                                                  sec98=self.COMMAND,
                                                  sec99=MANAGEMENT.TURN
                                                  )
        print(action_contents)
        try:
            a = int(input('セレクトコマンド>>>'))
            if a == 1:
                self.limit_break_1()
            elif a == 2:
                self.limit_break_2()
            elif a == 3:
                self.limit_break_3()
            elif a == 4:
                self.limit_break_4()
            elif a == 5:
                self.select_command()
            elif a == 6:
                self.select_limit()
        except IndexError:
            print('無効な入力です。')
            self.select_command()
