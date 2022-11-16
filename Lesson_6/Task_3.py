# Задайте последовательность цифр.
# Напишите программу, которая выведет список неповторяющихся элементов
# исходной последовательности.

# Использовать **лямбды/filter/map/zip/enumerate/list comprehension

# Пример:
# 47756688399943 -> [5]
# 1113384455229 -> [8,9]
# 1115566773322 -> []

from random import randint


number = input('Введите количество цифр последовательности от 0 до 30: ')

if number.isdigit() and 0 <= int(number) <= 30:
    number = int(number)

    sequence = ''.join([str(randint(1, 10))
                       for i in range(0, number)])

    result_list = [
        j for j in sequence if j not in sequence[sequence.find(j) + 1:]]

    print(
        f'Cписок неповторяющихся элементов последовательности [{sequence}] равен {result_list}')
else:
    print('Ошибка. Ввод в неверном формате, введено не числo или число в неверном диапазоне.')
