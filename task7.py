# с клавиатуры вводятся числа, ввод завершается числом 0.
# Определить минимальное из введённых чисел Фибоначчи.
# Вывести "нет", если чисел Фибоначчи в последовательности нет.
# Числа Фибоначчи – это последовательность чисел,
# которая начинается с двух единиц и каждое следующее число
# равно сумме двух предыдущих: 1, 1, 2, 3, 5, 8, 13, …

def is_fibonacci(n):
    """Проверяет, является ли число Фибоначчи."""
    a, b = 1, 1
    while a < n:
        a, b = b, a + b
    return a == n


def main():
    min_fib = float('inf')
    found_fib = False

    while True:
        number = int(input("Введите число (0 для завершения): "))

        if number == 0:
            break

        if is_fibonacci(number):
            found_fib = True
            if number < min_fib:
                min_fib = number

    if found_fib:
        print("Минимальное число Фибоначчи:", min_fib)
    else:
        print("нет")


if __name__ == "__main__":
    main()

