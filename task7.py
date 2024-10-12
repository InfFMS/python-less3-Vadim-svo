import math
a = int(input())
b = 9999999999999999999999999999999
while a != 0:
    if math.sqrt(5*a**2+4) == int(math.sqrt(5*a**2+4)) or math.sqrt(5*a**2-4) == int(math.sqrt(5*a**2-4)):
        if a < b:
            b = a
    a = int(input())

if b == 9999999999999999999999999999999:
    print('нет')
else:
    print(f'Минимальное число Фибоначчи: {b}')