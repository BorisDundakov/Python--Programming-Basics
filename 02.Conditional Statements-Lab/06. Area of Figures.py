# Да се напише програма, в която потребителят въвежда вида и размерите на геометрична фигура и пресмята
# лицето й. Фигурите са четири вида: квадрат (square), правоъгълник (rectangle), кръг (circle) и
# триъгълник (triangle). На първия ред на входа се чете вида на фигурата (square, rectangle, circle или
# triangle):
#  Ако фигурата е квадрат, на следващия ред се чете едно число - дължина на страната му;
#  Ако фигурата е правоъгълник, на следващите два реда четат две числа - дължините на страните му;
#  Ако фигурата е кръг, на следващия ред чете едно число - радиусът на кръга;
#  Ако фигурата е триъгълник, на следващите два реда четат две числа - дължината на страната му и
# дължината на височината към нея.
# Резултатът да се закръгли до 3 цифри след десетичната точка.
from math import pi

shape = str(input())

if shape == "square":
    side = float(input())
    result = (float(side * side))
    print(f'{result: .3f}')

if shape == "rectangle":
    a = float(input())
    b = float(input())
    result = (float(a * b))
    print(f'{result: .3f}')

if shape == "circle":
    r = float(input())
    result = (float(pi * r ** 2))
    print(f'{result: .3f}')

if shape == "triangle":
    a = float(input())
    h = float(input())
    result = (a * h / 2)
    print(f'{result: .3f}')
