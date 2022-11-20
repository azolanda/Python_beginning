# Напишите программу, которая принимает на вход число N и
# выдает набор произведений чисел от 1 до N.

# Использовать **лямбды/filter/map/zip/enumerate/list comprehension

# *Пример:*
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

def factorial(num):
    temp = 1
    for i in range(1, num + 1):
        temp *= i
    return temp


number = input("Введите натуральное число: ")

if number.isdigit() and int(number) > 0:
    factorial_list = list(
        map(lambda i: factorial(i), range(1, int(number) + 1)))
    print(
        f'Набор произведений чисел от 1 до {number} равно {factorial_list}')
else:
    print('Ошибка. Ввод в неверном формате. Введите натуральное число.')
