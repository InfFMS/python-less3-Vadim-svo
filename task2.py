# с клавиатуры вводятся числа, ввод завершается числом 0.
# Определить, сколько было введено двузначных натуральных чисел,
# и сколько других.

a = int(input())
c = 0
p = 0
while a != 0:
    if a > 9 and a < 100 or a > -100 and a < -9:
        c += 1
    else:
        p += 1
    a = int(input())

print(f'Двузначных чисел: {c} и Других чисел: {p}')