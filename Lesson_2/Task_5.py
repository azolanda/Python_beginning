# Реализуйте алгоритм перемешивания списка.

import random


def make_list(num):
    num_list = []
    for i in range(1, num + 1):
        num_list.append(round(random.uniform(-num, num)))
    return num_list


def mix_list(list):
    temp = 0
    for i in range(0, len(list)-1):
        new_pos = round(random.uniform(0, len(list) - 1))
        temp = list[new_pos]
        list[new_pos] = list[i]
        list[i] = temp
    return list


number = input('Введите натуральное число n: ')

if number.isdigit():
    number = int(number)
    number_list = make_list(number)
    print(f'Исходный список: {number_list}')
    print(f'Перемешанный список: {mix_list(number_list)}')
else:
    print('Ошибка. Ввод в неверном формате, введено не натуральное число. Введите натуральное число.')
