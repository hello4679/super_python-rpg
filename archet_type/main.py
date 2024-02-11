from template import AA
import BATTLE
import MANAGEMENT
import time


def select_player():
    try:
        chara = int(input(AA.SELECT_PLAYER))
        if chara == 1:
            MANAGEMENT.select_character = 1
        elif chara == 2:
            MANAGEMENT.select_character = 2
        elif chara == 3:
            MANAGEMENT.select_character = 3
    except ValueError:
        print('無効な入力です')
        select_player()


def game_start():
    print(AA.title)
    try:
        play = int(input('''
        >( info )プレイしますか？　
        はい　　＝＞1  
        いいえ　＝＞2
        '''))
        if play == 1:
            time.sleep(1)
            select_player()
            time.sleep(1)
            print(
                '( info )このゲームはフィクションであり実在の人物、団体とは一切の関係はありません')
            time.sleep(1)
            BATTLE.battle()
        elif play == 2:
            exit()
    except ValueError:
        exit()


game_start()
#BATTLE.battle()

