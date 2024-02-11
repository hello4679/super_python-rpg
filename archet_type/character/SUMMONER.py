import random
import time
from character import PLAYER
from template import UI
import MANAGEMENT
import STATUS


class Summoner(PLAYER.Player):
    def __init__(self,
                 name='召喚士',
                 hp=100,
                 mp=100,
                 ap=150,
                 power=25,
                 magic_power=150,
                 spirit_power=250,
                 defence_power=75,
                 luck=15
                 ):
        super().__init__(name, hp, mp, ap, power, magic_power, spirit_power,
                         defence_power, luck)
        self.COMMAND = '  SELECT COMMAND '

    def limit_break_1(self):
        if self.gauge_count >= 1:
            print(r'>\ \ \ ざ　ん　て　つ　け　ん / / /')
            x = int(self.power * 99)
            MANAGEMENT.physical_damage = x
            print(x)
            self.limit_count = 0
        else:
            print('>リミットゲージが足りません')
            self.select_limit()

    def limit_break_2(self):
        if self.gauge_count >= 2:
            print(r'>\ \ \ 転　生　の　炎 / / /')
            self.hp = self.upper_hp
            self.mp = self.upper_mp
            self.ap = self.upper_ap
            self.limit_count = 0
        else:
            print('>リミットゲージが足りません')
            self.select_limit()

    def limit_break_3(self):
        if self.gauge_count >= 3:
            print('転回始めるは、楔放つ歯車。一つ、二つ、三つ、四つ、……')
            time.sleep(1)
            print(
                '我が因果の枷持ちて……朧なる咆哮の下……深淵より劫罰の叫び響かせ……天に、現出せん！')
            time.sleep(1)
            print(r'>\ \ \ 聖　な　る　光 / / /')
            x = int(self.magic_power * 99)
            MANAGEMENT.physical_damage = x
            print(x)
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
            print(f'>{self.name}の詠唱')
            self.ap -= cost_ap
            self.limit_count += 200
        else:
            print('>APが足りない！！')
            self.select_job_action()

    def job_action_2(self):
        cost_ap = STATUS.AP_3
        if self.ap >= cost_ap:
            print(f'>{self.name}の犠牲召喚')
            self.ap -= cost_ap
            times_magic = int(self.magic_power * 2)
            harf_magic = int(self.magic_power * 0.5)
            MANAGEMENT.magic_damage = int(
                random.uniform(harf_magic, times_magic))
        else:
            print('>APが足りない！！')
            self.select_job_action()

    def job_action_3(self):
        cost_ap = STATUS.AP_1
        if self.ap >= cost_ap:
            print(f'>{self.name}の半召喚=魔剣')
            self.ap -= cost_ap
            MANAGEMENT.magic_damage = int((self.power * self.magic_power) / 2)
        else:
            print('>APが足りない！！')
            self.select_job_action()

    def job_action_4(self):
        cost_ap = STATUS.AP_1
        if self.ap >= cost_ap:
            print(f'>{self.name}の半召喚=纏剣')
            self.ap -= cost_ap
            self.hp += int((self.power * self.magic_power) / 2)
        else:
            print('>APが足りない！！')
            self.select_job_action()

    def select_job_action(self):
        self.limit_gauge(self.limit_count)
        self.show_limit()
        action_contents = UI.BATTLE_UI.substitute(sec1='詠唱　　　 ',
                                                  sec2='犠牲召喚　 ',
                                                  sec3='半召喚=魔剣',
                                                  sec4='半召喚=纏剣',
                                                  sec5=STATUS.AP_3,
                                                  sec6=STATUS.AP_3,
                                                  sec7=STATUS.AP_1,
                                                  sec8=STATUS.AP_1,
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
        action_contents = UI.BATTLE_UI.substitute(sec1='オーディン　　　　　　　',
                                                  sec2='フェニックス　　　　　　',
                                                  sec3='秘匿大軍神アレキサンダー',
                                                  sec4='               　　　',
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
