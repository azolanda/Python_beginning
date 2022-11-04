# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:
# - для k = 8 список будет выглядеть так:
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]

def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def nega_fib(n):
    if n == 0:
        return 1
    elif n == 1:
        return -1
    else:
        return nega_fib(n - 2) - nega_fib(n - 1)


def make_sequence(num):
    fib_list = []
    for i in range(0, num):
        fib_list.append(fib(i))
    fib_list.insert(0, 0)
    for j in range(0, num):
        fib_list.insert(0, nega_fib(j))
    return fib_list


number = input(
    'Введите число n для создания последовательности: ')

if number.isdigit() and int(number) >= 0:
    number = int(number)
    sequence = make_sequence(number)
    print(
        f'Последовательность для числа {number} равна {sequence}')
else:
    print('Ошибка. Ввод в неверном формате, введено не натуральное число. Введите натуральное число.')
