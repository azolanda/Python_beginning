# Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка,
# стоящих на нечётной позиции.

# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import random


def make_list(num):
    num_list = []
    for i in range(1, num + 1):
        num_list.append(round(random.uniform(-num, num)))
    return num_list


def odd_sum(list):
    sum = 0
    if len(list) == 0:
        return sum
    index = 0
    for i in list:
        if index % 2 == 1:
            sum += i
        index += 1
    return sum


number = input('Введите натуральное число n (кол-во элементов списка): ')

if number.isdigit() and int(number) >= 0:
    number = int(number)
    number_list = make_list(number)
    num_sum = odd_sum(number_list)
    print(
        f'Сумма элементов на нечетных позициях списка {number_list} равна {num_sum}')
else:
    print('Ошибка. Ввод в неверном формате, введено не натуральное число. Введите натуральное число.')
