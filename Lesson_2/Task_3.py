# Задайте список из n чисел последовательности (1 + 1/n)^n и выведите на экран их сумму.

# *Пример:*

#     Для n=4 {1: 2, 2: 2.25, 3: 2.37, 4: 2.44}
#     Сумма 9.06

def make_sequence(num):
    sequence = {}
    for i in range(1, num + 1):
        sequence[i] = round((1 + 1/i)**i, 2)
    return sequence


def sequence_sum(seq):
    sum = 0
    for i in seq:
        sum += seq[i]
    return sum


number = input('Введите натуральное число n: ')

if number.isdigit():
    seq_list = make_sequence(int(number))
    print(f'Для n = {number} {seq_list} сумма {sequence_sum(seq_list)}')
else:
    print('Ошибка. Ввод в неверном формате, введено не натуральное число. Введите натуральное число.')
