# с клавиатуры вводятся числа, ввод завершается числом 0.
# Определить минимальное и максимальное из введённых чисел.

a = int(input())
min = 999999999999999999999999999999999
max = -999999999999999999999999999999
while a != 0:
    if a > max and a !=0:
        max = a
    if a < min and a !=0:
        min = a
    a = int(input())
if min == 999999999999999999999999999999999 and max == -999999999999999999999999999999:
    print('Нет чисел для анализа.')
else:
    print(f'Минимальное число: {min}\nМаксимальное число: {max}')