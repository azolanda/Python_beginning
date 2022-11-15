# Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка,
# стоящих на нечётной позиции.

# Использовать **лямбды/filter/map/zip/enumerate/list comprehension

# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import random


number = input('Введите натуральное число n (кол-во элементов списка): ')

if number.isdigit() and int(number) >= 0:
    number = int(number)

    number_list = [round(random.uniform(-number, number))
                   for i in range(1, number + 1)]

    filtered_list = [number_list[i] for i in range(len(number_list)) if i % 2]

    sum = sum(filtered_list)

    print(
        f'Сумма элементов на нечетных позициях списка {number_list} равна {sum}')
else:
    print('Ошибка. Ввод в неверном формате, введено не натуральное число. Введите натуральное число.')
