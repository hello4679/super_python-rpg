import random
import numpy as np
from character import CHARACTER
from template import UI
import MANAGEMENT
import STATUS


class Player(CHARACTER.Character):
    def __init__(self,
                 name='未設定',
                 hp=100,
                 mp=100,
                 ap=100,
                 power=100,
                 magic_power=100,
                 spirit_power=100,
                 defence_power=100,
                 luck=10
                 ):
        super().__init__(name, hp, mp, ap, power, magic_power, spirit_power,
                         defence_power, luck)
        self.COMMAND = '  SELECT COMMAND '

    def no_config(self):
        print('未設定')
        self.select_command()

    def show_limit(self):
        if self.gauge_count >= 1:
            self.COMMAND = 'LIMIT IS READY!!'

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
            MANAGEMENT.enemy_total_damage = int(
                (MANAGEMENT.enemy_physical_damage
                 * (1 - (self.defence_power / 1000)))
                + MANAGEMENT.enemy_magic_damage
                * ((1 - (self.defence_power / 1000))
                   * (1 - (self.spirit_power / 1000))))
            #print(MANAGEMENT.enemy_physical_damage)
            #print(MANAGEMENT.enemy_magic_damage)
            #print(MANAGEMENT.enemy_total_damage)

            if MANAGEMENT.enemy_total_damage <= 0:
                MANAGEMENT.enemy_total_damage = 0
            self.hp -= MANAGEMENT.enemy_total_damage
            self.limit_count += MANAGEMENT.enemy_total_damage
            print(f'{self.name}に{MANAGEMENT.enemy_total_damage}ダメージ！！')
        else:
            print(f'{self.name}はひらりと躱した！！')
        if MANAGEMENT.enemy_total_damage > 0:
            MANAGEMENT.enemy_total_damage = 0
        MANAGEMENT.enemy_physical_damage = 0
        MANAGEMENT.enemy_magic_damage = 0

    # ================================　たたかう　================================

    def attack(self):
        print(f'>{self.name}のこうげき')
        harf_power = int(self.power * 0.5)
        MANAGEMENT.physical_damage = int(random.uniform(harf_power, self.power))

    # =================================　まほう　=================================

    # 攻撃魔法のテンプレート
    def magic_1(self):
        cost_mp = STATUS.MP_3
        if self.mp >= cost_mp:
            print(f'>{self.name}はルインを唱えた')
            self.mp -= cost_mp
            harf_magic_power = int(self.magic_power * 0.5)
            MANAGEMENT.magic_damage = int(
                random.uniform(harf_magic_power, self.magic_power))
        else:
            print('>MPが足りない！！')
            self.select_magic()

    # 回復魔法のテンプレート
    def magic_2(self):
        cost_mp = STATUS.MP_3
        if self.mp >= cost_mp:
            print(f'>{self.name}はケアルを唱えた')
            self.mp -= cost_mp
            harf_magic_power = int(self.magic_power * 0.5)
            cure_hp = int(random.uniform(harf_magic_power, self.magic_power))
            if cure_hp + self.hp > self.upper_hp:
                self.hp = self.upper_hp
                print(f'>>{self.name}のHPが全回復した！！')
            else:
                self.hp = cure_hp + self.hp
                print(f'>>{self.name}のHPが{cure_hp}回復した！！')

        else:
            print('>MPが足りない！！')
            self.select_magic()

    def magic_3(self):
        self.no_config()

    def magic_4(self):
        self.no_config()

    # =================================　アイテム　===============================

    def portion(self):
        cure_hp = 100
        if 'ポーション' in MANAGEMENT.PLAYER_INVENTORY:
            print(f'>{self.name}はポーションを使った！！')
            MANAGEMENT.PLAYER_INVENTORY.remove('ポーション')
            if cure_hp + self.hp > self.upper_hp:
                self.hp = self.upper_hp
                print(f'>>{self.name}のHPが全回復した！！')
            else:
                self.hp = cure_hp + self.hp
                print(f'>>{self.name}のHPが{cure_hp}回復した！！')
        else:
            print('>ポーションを持っていない！！')
            self.select_item()

    def ether(self):
        cure_mp = 100
        if 'エーテル' in MANAGEMENT.PLAYER_INVENTORY:
            print(f'>{self.name}はエーテルを使った！！')
            MANAGEMENT.PLAYER_INVENTORY.remove('エーテル')
            if cure_mp + self.mp > self.upper_mp:
                self.mp = self.upper_mp
                print(f'>>{self.name}のMPが全回復した！！')
            else:
                self.mp = cure_mp
                print(f'>>{self.name}のHPが{cure_mp}回復した！！')

        else:
            print('>エーテルを持っていない！！')
            self.select_item()

    def elixir(self):
        if 'エリクサー' in MANAGEMENT.PLAYER_INVENTORY:
            print(f'>{self.name}はエリクサーを使った！！')
            MANAGEMENT.PLAYER_INVENTORY.remove('エリクサー')
            self.hp = self.upper_hp
            self.mp = self.upper_mp
            self.ap = self.upper_ap
            print(f'>>{self.name}は元気になった！')
        else:
            print('>エリクサーを持っていない！！')
            self.select_item()

    def grenade(self):
        if '手榴弾' in MANAGEMENT.PLAYER_INVENTORY:
            print(f'>{self.name}は手榴弾を使った！！')
            MANAGEMENT.PLAYER_INVENTORY.remove('手榴弾')
            MANAGEMENT.physical_damage = 100
        else:
            print('>手榴弾を持っていない！！')
            self.select_item()

    # ==============================　リミットブレイク　============================

    def limit_break_1(self):
        self.no_config()

    def limit_break_2(self):
        self.no_config()

    def limit_break_3(self):
        self.no_config()
    def limit_break_4(self):
        self.no_config()

    def limit_gauge(self, limit_count):
        if limit_count >= 1500:
            self.gauge_count = 4
            self.gauge = '////////|'
        elif limit_count >= 1000:
            self.gauge_count = 3
            self.gauge = '//////|  '
        elif limit_count >= 600:
            self.gauge_count = 2
            self.gauge = '////|    '
        elif limit_count >= 300:
            self.gauge_count = 1
            self.gauge = '//|      '

    # ===============================　ジョブアクション　===========================

    def job_action_1(self):
        self.no_config()

    def job_action_2(self):
        self.no_config()

    def job_action_3(self):
        self.no_config()

    def job_action_4(self):
        self.no_config()

    # ================================ コマンド入力  ==============================

    def select_command(self):
        self.limit_gauge(self.limit_count)
        self.show_limit()
        action_contents = UI.BATTLE_UI.substitute(sec1='たたかう',
                                                  sec2='まほう　',
                                                  sec3='ジョブ　',
                                                  sec4='アイテム',
                                                  sec5='　',
                                                  sec6='　',
                                                  sec7='　',
                                                  sec8='　',
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
                self.attack()
            elif a == 2:
                self.select_magic()
            elif a == 3:
                self.select_job_action()
            elif a == 4:
                self.select_item()
            elif a == 5:
                self.select_command()
            elif a == 6:
                self.select_limit()
        except ValueError:
            print('無効な入力です')
            self.select_command()

    def select_magic(self):
        self.limit_gauge(self.limit_count)
        self.show_limit()
        magic_contents = UI.BATTLE_UI.substitute(sec1='ルイン　',
                                                 sec2='ケアル　',
                                                 sec3='　　　　',
                                                 sec4='　　　　',
                                                 sec5=STATUS.MP_3,
                                                 sec6=STATUS.MP_3,
                                                 sec7=' ',
                                                 sec8=' ',
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
        print(magic_contents)
        try:
            a = int(input('セレクトコマンド>>>'))
            if a == 1:
                self.magic_1()
            elif a == 2:
                self.magic_2()
            elif a == 3:
                self.magic_3()
            elif a == 4:
                self.magic_4()
            elif a == 5:
                self.select_command()
            elif a == 6:
                self.select_limit()
        except IndexError:
            print('無効な入力です')
            self.select_command()

    def select_item(self):
        self.limit_gauge(self.limit_count)
        self.show_limit()
        items = {}
        for item in MANAGEMENT.PLAYER_INVENTORY:
            items[item] = items.get(item, 0) + 1
        item_contents = UI.BATTLE_UI.substitute(sec1='ポーション',
                                                sec2='エーテル　',
                                                sec3='エリクサー',
                                                sec4='手榴弾　　',
                                                sec5=items.get('ポーション'),
                                                sec6=items.get('エーテル'),
                                                sec7=items.get('エリクサー'),
                                                sec8=items.get('手榴弾'),
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
        print(item_contents)

        try:
            a = int(input('セレクトコマンド>>>'))
            if a == 1:
                self.portion()
            elif a == 2:
                self.ether()
            elif a == 3:
                self.elixir()
            elif a == 4:
                self.grenade()
            elif a == 5:
                self.select_command()
            elif a == 6:
                self.select_limit()
        except IndexError:
            print('無効な入力です')
            self.select_command()

    def select_limit(self):
        self.limit_gauge(self.limit_count)
        self.show_limit()
        action_contents = UI.BATTLE_UI.substitute(sec1='超究武神覇斬　　　　',
                                                  sec2='ファントムソード召喚',
                                                  sec3='オーバークロック　　',
                                                  sec4='　　　　　　　　　　',
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

    def select_job_action(self):
        self.limit_gauge(self.limit_count)
        self.show_limit()
        action_contents = UI.BATTLE_UI.substitute(sec1='',
                                                  sec2='',
                                                  sec3='',
                                                  sec4='',
                                                  sec5='　',
                                                  sec6='　',
                                                  sec7='　',
                                                  sec8='　',
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
