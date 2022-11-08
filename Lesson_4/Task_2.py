# Задайте натуральное число N.
# Напишите программу, которая составит список простых множителей числа N.

def get_primes(num):
    data = [True for i in range(1, num + 1)]

    for i in range(1, len(data)):
        if not num % (i + 1):
            for j in range(i + i + 1, len(data), i + 1):
                data[j] = False
        else:
            data[i] = False
    return [i + 1 for i in range(0, len(data)) if data[i]]


number = input('Введите натуральное число N от 1 до 1000: ')

if number.isdigit() and 0 < int(number) <= 1000:
    number = int(number)
    primes = get_primes(number)

    print(
        f'Cписок простых множителей числа {number} равен {primes}')
else:
    print('Ошибка. Ввод в неверном формате, введено не натуральное числo или число в неверном диапазоне.')
