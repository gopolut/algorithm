# найти простые числа
# 1 O(n)

# В цикле идем по всем подряд числам со 2 до n
# Цикл работает до тех пор пока i=2 меньше чем заданное число n
# n=3, i=2
# 3 делим на 2: результат == 0? Нет.
# Идем дальше к i+1
# i=3 i становится ранвным n и цикл прекращается 
# возвращается True - число 3 простое

# def is_prime(n):
#     if n == 1:
#         return False
#     i = 2
#     while i < n:
#         if n % i == 0:
#             return False
#         i = i + 1
#     return True

# n = 2
# print(is_prime(n))

# 2 O(n)
# Проверять числа, которые больше чем sqrt n, 
# необязательно. Если у числа n есть делитель, больший чем sqrt n,
# то существует и делитель, меньший sqrt n.
# А его мы проверим раньше.

def is_prime(n):
    if n == 1:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i = i + 1
    return True


n = 8
print(is_prime(n))
