# Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.

# Пример:

# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

import math

cords_a = list(
    input('Enter first cords - two numbers with space separator: ').split(' '))
cords_b = list(
    input('Enter second cords - two numbers with space separator: ').split(' '))

ab_distance = math.sqrt(
    (int(cords_b[0]) - int(cords_a[0]))**2 + (int(cords_b[1]) - int(cords_a[1]))**2)
print(round(ab_distance, 2))
