def build_matryoshka(size, n):
    if n >= 1:
        print(f"Создаём низ матрёшки размера {size}.")
        build_matryoshka(size - 1, n - 1)
        print(f"Создаём верх матрешки размера {size}.")
    else:
        return


def fact(x):
    if x == 1:
        return 1
    else:
        # print(x * fact(x - 1))
        return x * fact(x - 1)


def as_binary_string(n):
    if n < 0:
        return "-" + as_binary_string(-n)
    if n == 0 or n == 1:
        return str(n)
    last_digit = n % 2
    return as_binary_string(n // 2) + str(last_digit)


if __name__ == '__main__':
    # command, input_values = input().split()
    # print('c:', command)
    # print('inp:', input_values)
    # build_matryoshka(int(command), int(input_values))

    # print(as_binary_string(int(input())))
    print(fact(3))
