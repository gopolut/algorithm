'''
G. Работа из дома
Переводит целого числа из десятичной системы в двоичную
'''


# 46ms | 4.01Mb
def to_binary(number: int) -> str:
    a = number
    binary = ''
    if number == 0:
        return 0
    while a > 0:
        binary += str(a % 2)
        a = a//2
    return binary[::-1]


def read_input() -> int:
    return int(input().strip())


print(to_binary(read_input()))
