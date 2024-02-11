import random
import time
from character import PLAYER
from template import UI
import MANAGEMENT
import STATUS


class Thief(PLAYER.Player):
    def __init__(self,
                 name='盗賊',
                 hp=100,
                 mp=100,
                 ap=100,
                 power=75,
                 magic_power=100,
                 spirit_power=150,
                 defence_power=75,
                 luck=25
                 ):
        super().__init__(name, hp, mp, ap, power, magic_power, spirit_power,
                         defence_power, luck)
        self.COMMAND = '  SELECT COMMAND '

    def limit_break_1(self):
        if self.gauge_count >= 1:
            print(r'>\ \ \ ついでにぬすむ / / /')
            if MANAGEMENT.ENEMY_INVENTORY is not []:
                x = MANAGEMENT.ENEMY_INVENTORY.pop()
                MANAGEMENT.PLAYER_INVENTORY.append(x)
                print(f'>{self.name}は{x}を盗んだ！！')
                MANAGEMENT.physical_damage = int(self.power*5)

            else:
                print('>何も持っていない！！')
                self.select_item()
        else:
            print('>リミットゲージが足りません')
            self.select_limit()

    def limit_break_2(self):
        if self.gauge_count >= 2:
            print(r'>\ \ \ソリューション９ / / /')
            for i in range(9):
                MANAGEMENT.magic_damage += 99
        else:
            print('>リミットゲージが足りません')
            self.select_limit()

    def limit_break_3(self):
        self.no_config()

    def limit_break_4(self):
        if self.gauge_count >= 4:
            print(r'>\ \ \ NONE / / /')
            self.limit_count = 0
        else:
            print('>リミットゲージが足りません')
            self.select_limit()

    def job_action_1(self):
        cost_ap = STATUS.AP_1
        if self.ap >= cost_ap:
            if MANAGEMENT.ENEMY_INVENTORY is not []:
                x = MANAGEMENT.ENEMY_INVENTORY.pop()
                MANAGEMENT.PLAYER_INVENTORY.append(x)
                print(f'>{self.name}は{x}を盗んだ！！')
            else:
                print('>何も持っていない！！')
                self.select_job_action()
        else:
            print('>APが足りない！！')
            self.select_job_action()

    def job_action_2(self):
        cost_ap = STATUS.AP_1
        if self.ap >= cost_ap:
            if MANAGEMENT.ENEMY_INVENTORY is not []:
                x = MANAGEMENT.ENEMY_INVENTORY
                print(x)
            else:
                print('>何も持っていない！！')
                self.select_item()
        else:
            print('>APが足りない！！')
            self.select_job_action()

    def job_action_3(self):
        cost_ap = STATUS.AP_3
        if self.ap >= cost_ap:
            print(f'>{self.name}のみだれうち')
            self.ap -= cost_ap
            harf_power = int(self.power * 0.5)
            for i in range(5):
                MANAGEMENT.physical_damage += int(
                    random.uniform(self.power, harf_power))
                print('ボコスカ')
        else:
            print('>APが足りない！！')
            self.select_job_action()

    def job_action_4(self):
        cost_ap = STATUS.AP_3
        if self.ap >= cost_ap:
            print(f'>{self.name}はポッケのへそくりを使った')
            self.ap -= cost_ap
            self.hp += 200
            print('あっ...')
            print(r'''
        ＊＊
        /＊
  ,--./,-.
 / 　      \
 \        /    
  `._,._,'

            ''')
            time.sleep(1)
            print(r'''
                 ＊   ＊＊
                  ***＊
              ,--./,-.　
             / 　      \
             \        /    
              `._,._,'

                        ''')
            time.sleep(1)
            print('ドッカーーン')
            MANAGEMENT.physical_damage = 100
        else:
            print('>APが足りない！！')
            self.select_job_action()

    def select_job_action(self):
        self.limit_gauge(self.limit_count)
        self.show_limit()
        action_contents = UI.BATTLE_UI.substitute(sec1='ぬすむ　　',
                                                  sec2='みやぶる　',
                                                  sec3='窮鼠猫噛　',
                                                  sec4='へそくり　',
                                                  sec5=STATUS.AP_1,
                                                  sec6=STATUS.AP_1,
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
        action_contents = UI.BATTLE_UI.substitute(sec1='ついでにぬすむ ',
                                                  sec2='ソリューション9',
                                                  sec3='　　　　　　　　',
                                                  sec4='　　　　　　　　',
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