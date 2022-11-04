# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

import random


def make_list(num):
    num_list = []
    for i in range(1, num + 1):
        num_list.append(round(random.uniform(-num, num)))
    return num_list


def pair_multiple(list):
    mult_list = []
    j = len(list) - 1
    high_border = int(len(list)/2)
    if len(list) % 2 == 1:
        high_border += 1
    for i in range(0, high_border):
        mult_list.append(list[i] * list[j])
        j -= 1
    return mult_list


number = input('Введите натуральное число n (кол-во элементов списка): ')

if number.isdigit() and int(number) >= 0:
    number = int(number)
    number_list = make_list(number)
    multiple_list = pair_multiple(number_list)
    print(
        f'Произведение пар чисел списка {number_list} равно {multiple_list}')
else:
    print('Ошибка. Ввод в неверном формате, введено не натуральное число. Введите натуральное число.')
