#с клавиатуры вводятся числа, ввод завершается числом 0.
# Определить, сколько было введено положительных
# и сколько отрицательных чисел.

a = int(input())
c = 0
p = 0
while a != 0:
    if a > 0:
        c += 1
    else:
        p += 1
    a = int(input())

print(f'Положительных чисел: {c} и Отрицательных чисел: {p}')