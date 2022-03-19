from typing import List
'''
J. Факторизация
'''
# 68ms | 4.01Mb

def factorize(number: int) -> List[int]:
    # перебрать все простоые числа от 2 до sqrt(number)
    s = number ** 0.5
    l = []
    divisor = 2

    while divisor <= s:
        remainder = number % divisor
        # if number % divisor возвращает True/False
        if remainder == 0:
            number = number/divisor
            l.append(divisor)
        else:
            divisor += 1

    if number > 1:
        l.append(int(number))
    return l

result = factorize(int(input()))
print(" ".join(map(str, result)))
