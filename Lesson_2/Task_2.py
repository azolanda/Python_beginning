# Напишите программу, которая принимает на вход число N и
# выдает набор произведений чисел от 1 до N.

# *Пример:*

# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

def factorial(num):
    temp = 1
    for i in range(1, num + 1):
        temp *= i
    return temp


def make_factorial_list(num):
    factorial_list = []
    for i in range(1, num + 1):
        factorial_list.append(factorial(int(i)))
    return factorial_list


number = input("Введите натуральное число: ")

if number.isdigit() and int(number) > 0:
    print(
        f'Набор произведений чисел от 1 до {number} равно {make_factorial_list(int(number))}')
else:
    print('Ошибка. Ввод в неверном формате. Введите натуральное число.')
