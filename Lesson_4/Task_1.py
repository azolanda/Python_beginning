# Вычислить число Пи c заданной точностью d
# Пример:
# при d = 0.001, π = 3.141
# при d = 0.1, π = 3.1
# при d = 0.00001, π = 3.14154
# d от 0.1 до 0.0000000001

# !!ВНИМАНИЕ
# !!! не использовать константу math.pi


from decimal import *
from math import factorial as fact


def is_number(num):
    num = num.replace('.', '').replace(' ', '')
    return num.isdigit()


def count_precision(str):
    count_prec = 1
    for i in range(len(str)):
        if str[i] == '.':
            count_prec = len(str[i + 1:])
    return count_prec


def chudnovsky_pi(d):
    # вычисление числа Пи по алгоритму Чудновского
    pi = Decimal(0)
    k = 0
    while k < d:
        pi += (Decimal(-1)**k) * (Decimal(fact(6 * k)) / ((fact(k)**3)
                                                          * (fact(3 * k))) * (13591409 + 545140134 * k) / (640320**(3 * k)))
        k += 1
    pi = pi * Decimal(10005).sqrt() / 4270934400
    pi = pi**(-1)
    return pi


precision = input(
    'Введите необходимую точность числа Пи от 0.0000000001 до 0.1: ')
if is_number(precision) and 0.0000000001 <= float(precision) <= 0.1:
    d = count_precision(precision)
    pi_num = chudnovsky_pi(d).quantize(Decimal(precision), ROUND_FLOOR)
    print(f'Число Пи с точностью {precision} равно {pi_num}')
else:
    print("Ошибка. Введено не число или число в неверном диапазоне.")
