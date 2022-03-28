'''
B. Чётные и нечётные числа
https://contest.yandex.ru/contest/23389/problems/
'''
# 46ms | 4.02Mb


def check_parity(a: int, b: int, c: int) -> bool:
    a = a % 2 + b % 2 + c % 2
    if a == 0 or a == 3:
        return True


def print_result(result: bool) -> None:
    if result:
        print("WIN")
    else:
        print("FAIL")

a, b, c = map(int, input().strip().split())
print_result(check_parity(a, b, c))
