# Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета.
# Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота
# b) Подумайте как наделить бота "интеллектом"

import random as rand
import time


def human_player(move, sweets, player):
    while not 0 < move < 29 or not sweets - move >= 0:
        move = input(
            f'Введите кол-во конфет, которые забирает {player} - число от 1 до 28:   ')
        if move.isdigit():
            move = int(move)
        else:
            move = 0
            print('Вы ввели не число, введите число от 1 до 28')

    if not sweets - move < 0 and 0 < move < 29:
        sweets -= move

    move = 0

    if sweets <= 0:
        print(f'Выиграл {player}!')
    else:
        print(f'На столе осталось {sweets} конфет')

    return sweets


def bot_player(move, sweets, player):
    print(f'{player} думает...')

    time.sleep(2)

    move = int(rand.uniform(1, 28))

    if sweets - move < 0:
        while not sweets - move >= 0:
            move = int(rand.uniform(1, 28))

    sweets -= move

    print(f'{player} забрал {move} конфет(ы)')

    move = 0

    if sweets <= 0:
        print(f'Выиграл {player}!')
    else:
        print(f'На столе осталось {sweets} конфет')

    return sweets


def clever_bot_player(move, sweets, player):
    print(f'{player} думает...')

    time.sleep(2)

    if sweets <= 28:
        move = sweets
    else:
        if sweets % 29 == 0:
            move = 28
        else:
            move = sweets % 29

    sweets -= move

    print(f'{player} забрал {move} конфет(ы)')

    move = 0

    if sweets <= 0:
        print(f'Выиграл {player}!')
    else:
        print(f'На столе осталось {sweets} конфет')

    return sweets


sweets = 87
game_mode = ''
while not (game_mode == '1' or game_mode == '2' or game_mode == '3'):
    game_mode = input(
        'Выбрать режим игры: 1 - два игрока; 2 - игра против бота; 3 - игра с "умным" ботом.\nВведите 1, 2 или 3:   ')
move_1 = 0
move_2 = 0
print(f'На столе {sweets} конфет(ы)')

if game_mode == '1':
    while not sweets <= 0:
        sweets = human_player(move_1, sweets, 'ПЕРВЫЙ игрок')

        if sweets > 0:
            sweets = human_player(move_2, sweets, 'ВТОРОЙ игрок')

if game_mode == '2':
    while not sweets <= 0:
        sweets = human_player(move_1, sweets, 'ЧЕЛОВЕК')

        if sweets > 0:
            sweets = bot_player(move_2, sweets, 'БОТ')

if game_mode == '3':
    while not sweets <= 0:
        sweets = human_player(move_1, sweets, 'ЧЕЛОВЕК')

        if sweets > 0:
            sweets = clever_bot_player(move_2, sweets, 'ОЧЕНЬ УМНЫЙ БОТ')
