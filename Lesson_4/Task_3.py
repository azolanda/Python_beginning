# Задайте последовательность цифр.
# Напишите программу, которая выведет список неповторяющихся элементов
# исходной последовательности.
# Пример:
# 47756688399943 -> [5]
# 1113384455229 -> [8,9]
# 1115566773322 -> []

import random


def make_sequence(num):
    num_sequence = ''
    for i in range(0, num):
        num_sequence += str(int(random.uniform(1, 10)))
    return num_sequence


def unic_sequence(sequence):
    for j in sequence:
        index = sequence.find(j)

        if j in sequence[index + 1:]:
            sequence = sequence.replace(j, '')
    return list(sequence)


number = input('Введите количество цифр последовательности от 0 до 30: ')

if number.isdigit() and 0 <= int(number) <= 30:
    number = int(number)
    sequence = make_sequence(number)
    result_list = unic_sequence(sequence)

    print(
        f'Cписок неповторяющихся элементов последовательности [{sequence}] равен {result_list}')
else:
    print('Ошибка. Ввод в неверном формате, введено не числo или число в неверном диапазоне.')
