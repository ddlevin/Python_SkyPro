import math

side = float(input("Введите сторону квадрата: "))


def square(side):
    area = side * side
    if side % 1 != 0 or side % 1 != 0:
        area = math.ceil(area)
    return area


print("Площадь:", square(side))
