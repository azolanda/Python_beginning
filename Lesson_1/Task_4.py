# Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).

def get_cords_range(quarter_number):
    if quarter_number == 1:
        print('x:(0, 100) y:(0, 100)')
    elif quarter_number == 2:
        print('x:(0, -100) y:(0, 100)')
    elif quarter_number == 3:
        print('x:(0, -100) y:(0, -100)')
    elif quarter_number == 4:
        print('x:(0, 100) y:(0, -100)')
    else:
        print('Error. You should enter number of quarter in range from 1 to 4')


number = int(input('Enter number of quarter in range from 1 to 4: '))
get_cords_range(number)
