# с клавиатуры вводятся числа, ввод завершается числом 0.
# Определить сумму тех введённых чисел, которые делятся на 5.

a = int(input())
s = 0
while a != 0:
    if a % 5 == 0:
        s += a
    a = int(input())
print(f'Сумма чисел, делящихся на 5: {s}')