# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# *Пример:*

# - 6782 -> 23
# - 0,56 -> 11

def number_sum(num):
    sum = 0
    for i in num:
        sum += int(i)
    return sum


number = input("Введите число: ")
number = number.replace('-', '').replace(',',
                                         '').replace('.', '').replace(' ', '')

if number.isdigit():
    print(number_sum(number))
else:
    print("Ошибка. Вы ввели не число, введите число.")
