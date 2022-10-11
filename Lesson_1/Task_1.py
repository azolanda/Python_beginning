# Напишите программу, которая принимает на вход цифру, обозначающую день недели,
# и проверяет, является ли этот день выходным.
# Пример:

# - 6 -> да
# - 7 -> да
# - 1 -> нет

def is_weekend(num):
    weekday = list(range(1, 6))
    if num == 6 or num == 7:
        print('yes')
    elif num in weekday:
        print('no')
    else:
        print('Error, you num is out of range. Enter correct num in range from 1 to 7.')


num_day = int(input('Enter day of a week in the range from 1 to 7: '))
is_weekend(num_day)
