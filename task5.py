# с клавиатуры вводятся числа, ввод завершается числом 0.
# Определить, среднее арифметическое тех введённых чисел,
# которые являются степенями числа 2.
# Вывести "нет", если таких чисел нет.

a = int(input())
s = 0
c = 0
while a != 0:
    for i in range (1, a):
        t = 2 ** i
        if a == t:
            c += 1
            s += a
    a = int(input())
if c != 0:
    print(f'Среднее арифметическое чисел, являющихся степенями двойки: {(s / c)}')
else: print('нет')