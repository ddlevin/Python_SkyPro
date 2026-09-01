import math


def square(side):
    area = side * side
    if side % 1 != 0:

        area = math.ceil(area)
    return area


side = float(input("Введите сторону квадрата: "))
print(f"Площадь: {square(side)}")
