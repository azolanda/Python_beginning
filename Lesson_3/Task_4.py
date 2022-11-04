# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

def make_binary(num):
    binary = ''
    if num == 0 or num == 1:
        return str(num)
    while num >= 2:
        binary = str(int(num % 2)) + binary
        num = int(num / 2)
        if num == 1:
            binary = str(num) + binary
    return binary


number = input(
    'Введите число n для перевода в двоичную систему счисления: ')

if number.isdigit() and int(number) >= 0:
    number = int(number)
    binary_num = make_binary(number)
    print(
        f'В двоичной системе счисления введенное число равно {binary_num}')
else:
    print('Ошибка. Ввод в неверном формате, введено не натуральное число. Введите натуральное число.')
