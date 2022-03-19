from typing import Dict


# рекурсия
def fib(n: int) -> int:
    if n < 2:
        return n
    # a = fib(n - 2)
    # b = fib(n - 1)
    # c = a + b

    return fib(n - 2) + fib(n - 1)


# мемоизация
memo: Dict[int, int] = {0: 0, 1: 1}


def fib3(n):
    memo
    if n not in memo:
        memo[n] = fib3(n-1) + fib3(n - 2)
    return memo[n]


if __name__ == '__main__':
    # print(fib(3))
    print(fib3(5))
