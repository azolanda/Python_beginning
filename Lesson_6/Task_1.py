# Задайте список из n чисел последовательности (1 + 1/n)^n и выведите на экран их сумму.
# Использовать **лямбды/filter/map/zip/enumerate/list comprehension

# *Пример:*

#     Для n=4 {1: 2, 2: 2.25, 3: 2.37, 4: 2.44}
#     Сумма 9.06

def sequence_sum(seq):
    sum = 0
    for i in seq:
        sum += seq[i]
    return sum


num = input('Введите натуральное число n: ')

if num.isdigit() and int(num) > 0:
    seq_list = [round((1 + 1/i)**i, 2) for i in range(1, int(num) + 1)]
    seq = dict(zip([i for i in range(1, len(seq_list) + 1)], seq_list))

    sequence_sum = sum(map(lambda i: seq[i], seq))

    print(f'Для n = {num} {seq} сумма {sequence_sum}')
else:
    print('Ошибка. Ввод в неверном формате, введено не натуральное число. Введите натуральное число.')
