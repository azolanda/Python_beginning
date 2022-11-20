# Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между максимальным и
# минимальным значением дробной части элементов.

# Использовать **лямбды/filter/map/zip/enumerate/list comprehension

# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random
import math


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


number = input('Введите натуральное число n (кол-во элементов списка): ')

if number.isdigit() and int(number) >= 0:
    number = int(number)

    num_list = [round(random.uniform(-number, number), 2)
                for i in range(1, number + 1)]

    fract_list = [round(abs(math.modf(i)[0]),  2) for i in num_list]

    extremes = min_max(fract_list)
    if extremes == None:
        print(
            f'Не определить разницу между max и min значением дробной части элементов списка {num_list}, список пустой')
    else:
        fract_diff = round(extremes[1] - extremes[0], 2)
        print(
            f'Разница между max ({extremes[1]}) и min ({extremes[0]}) значением дробной части элементов списка {num_list} равно {fract_diff}')
else:
    print('Ошибка. Ввод в неверном формате, введено не натуральное число. Введите натуральное число.')
