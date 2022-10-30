# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции вводятся с клавиатуры.

import random


def make_list(num):
    num_list = []
    for i in range(1, num + 1):
        num_list.append(round(random.uniform(-num, num)))
    return num_list


def multiply_elements(list):
    pos_a = input(
        f'Введите позицию в списке первого множителя от 0 до {number - 1}: ')
    pos_b = input(
        f'Введите позицию в списке второго множителя от 0 до {number - 1}: ')

    if pos_a.isdigit() and pos_b.isdigit() and 0 <= int(pos_a) <= number - 1 and 0 <= int(pos_b) <= number - 1:
        multiply = list[int(pos_a)] * list[int(pos_b)]
        print(
            f'Произведение элементов списка {list} на позициях {pos_a} и {pos_b} равно {multiply}')
    else:
        print(
            f'Ошибка. Введена позиция в неверном формате. Введите числа от 0 до {number - 1}.')


number = input('Введите натуральное число n: ')

if number.isdigit() and int(number) > 0:
    number = int(number)
    number_list = make_list(number)
    multiply_elements(number_list)
else:
    print('Ошибка. Ввод в неверном формате, введено не натуральное число. Введите натуральное число.')
