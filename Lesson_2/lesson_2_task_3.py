import math

def square():
    side = float(input("Сторона = "))
    area = (side * side)
    if (side % 2 == 0):
        return math.trunc(area)
    else: 
        return math.ceil(area)
 

print("Квадрат = ", square())
    