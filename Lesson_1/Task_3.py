# Напишите программу, которая принимает на вход координаты точки (X и Y),
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
# в которой находится эта точка.

# Пример:

# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

def get_quarter_number(x, y):
    if x > 0 and y > 0:
        print(f'({x}, {y}): quarter 1')
    elif x < 0 and y > 0:
        print(f'({x}, {y}): quarter 2')
    elif x < 0 and y < 0:
        print(f'({x}, {y}): quarter 3')
    elif x > 0 and y < 0:
        print(f'({x}, {y}): quarter 4')
    else:
        print('Error. You should enter numbers is not equal 0')

x_cord = int(input("Enter x coords, x is not equal 0: "))
y_cord = int(input("Enter y coords, y is not equal 0: "))

get_quarter_number(x_cord, y_cord)