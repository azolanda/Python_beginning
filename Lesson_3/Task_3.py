# Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между максимальным и
# минимальным значением дробной части элементов.

# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random
import math


def make_list(num):
    num_list = []
    for i in range(1, num + 1):
        num_list.append(round(random.uniform(-num, num), 2))
    return num_list


def make_fract_list(list):
    fract_list = []
    for i in list:
        fract_list.append(round(abs(math.modf(i)[0]),  2))
    return fract_list


def min_max(list):
    if len(list) == 0:
        return None
    max = list[0]
    min = list[0]
    for i in range(0, len(list) - 1):
        if min > list[i + 1]:
            min = list[i + 1]
        if max < list[i + 1]:
            max = list[i + 1]
    return (min, max)


def fract_difference(min_max):
    return min_max[1] - min_max[0]


number = input('Введите натуральное число n (кол-во элементов списка): ')

if number.isdigit() and int(number) >= 0:
    number = int(number)
    number_list = make_list(number)
    fract_list = make_fract_list(number_list)
    if min_max(fract_list) == None:
        print(
            f'Не определить разницу между max и min значением дробной части элементов списка {number_list}, список пустой')
    else:
        fract_diff = fract_difference(min_max(fract_list))
        print(
            f'Разница между max ({min_max(fract_list)[1]}) и min ({min_max(fract_list)[0]}) значением дробной части элементов списка {number_list} равно {fract_diff}')
else:
    print('Ошибка. Ввод в неверном формате, введено не натуральное число. Введите натуральное число.')
