import random
import time

from character import ENEMY, KNIGHT, SUMMONER, THIEF
import MANAGEMENT
from template import AA


def show_enemy():
    print(AA.enemy_art)


def effect_1():
    time.sleep(1)
    print('''
    ・
    ・
    ・''')


def battle():
    if MANAGEMENT.select_character == 1:
        player = THIEF.Thief(MANAGEMENT.chara_name_1)
    if MANAGEMENT.select_character == 2:
        player = KNIGHT.Knight(MANAGEMENT.chara_name_2)
    if MANAGEMENT.select_character == 3:
        player = SUMMONER.Summoner(MANAGEMENT.chara_name_3)
    enemy = ENEMY.Enemy('魔導兵', )

    num_turn = random.random()

    def player_turn():
        show_enemy()
        player.limit_gauge(player.limit_count)
        player.select_command()
        enemy.damaged()

    def enemy_turn():
        enemy.enemy_action()
        player.damaged()

    if num_turn >= 0.5:
        while True:
            player_turn()
            if player.hp <= 0:
                print(AA.gam)
                break
            if enemy.hp <= 0:
                print(AA.vic)
                break

            effect_1()

            enemy_turn()
            if player.hp <= 0:
                print(AA.gam)
                break
            if enemy.hp <= 0:
                print(AA.vic)
                break

            effect_1()

            MANAGEMENT.TURN += 1
    else:
        show_enemy()
        print('不意をつかれた！！')
        while True:
            enemy_turn()
            if player.hp <= 0:
                print(f'{player.name}は死亡した。。。')
                print(AA.gam)
                break
            if enemy.hp <= 0:
                print(f'{enemy.name}を倒した！！')
                print(AA.vic)
                break

            effect_1()

            player_turn()
            if player.hp <= 0:
                print(f'{player.name}は死亡した。。。')
                print(AA.gam)
                break
            if enemy.hp <= 0:
                print(AA.vic)
                print(f'{enemy.name}を倒した！！')
                break

            effect_1()

            MANAGEMENT.TURN += 1
