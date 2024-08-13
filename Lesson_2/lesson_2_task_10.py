import math

def bank():
    x = int(input("Сумма вложения: "))
    y = int(input("На сколько лет? "))
    stavka = 1.1**y
    summa = x * stavka
    return math.trunc(summa)


print(bank())
