from typing import Tuple

'''
H. Двоичная система
'''

# 78ms | 4.07Mb
def get_sum(first_number: str, second_number: str) -> str:
    
    # Определяем число с минимальным и максимальным кол-вом разрядов
    if len(first_number) < len(second_number):
        min_num = first_number[::-1]
        max_num = second_number[::-1]
    else:
        min_num = second_number[::-1]
        max_num = first_number[::-1]
    
    # для отладки
    m = len(min_num)-1
    l = len(max_num)-1

    i = 0
    j = 0
    next_digit = 0  # следующий разряд
    binary_sum = '' # сумма 2-х двоичных чисел

    while i <= len(max_num)-1:
        if int(max_num[i]) + int(min_num[j]) + next_digit == 0:
            binary_sum += '0'
            next_digit = 0
        elif int(max_num[i]) + int(min_num[j]) + next_digit == 1:
            binary_sum += '1'
            next_digit = 0
        elif int(max_num[i]) + int(min_num[j]) + next_digit == 2:
            if i == len(max_num)-1:
                binary_sum += '01'
            else:
                binary_sum += '0'
                next_digit = 1
        elif int(max_num[i]) + int(min_num[j]) + next_digit == 3:
            if i == len(max_num)-1:
                binary_sum += '11'
            else:
                binary_sum += '1'
                next_digit = 1

        if i >= len(min_num)-1:
            j = 0
            min_num = '0'
            i += 1
        else:
            j += 1
            i += 1

    return binary_sum[::-1]

def read_input() -> Tuple[str, str]:
    first_number = input().strip()
    second_number = input().strip()
    return first_number, second_number

first_number, second_number = read_input()
print(get_sum(first_number, second_number))


# Перевод из двоичной в десятичную
    # a = len(first_number) - 1
    # b = len(second_number) - 1
    # res1 = 0
    # res2 = 0

    # for i in first_number:
    #     if int(i) != 0:
    #         res1 += int(i) * (2 ** a)
    #     a -= 1
    # print(res1)
    
    # for j in second_number:
    #     if int(j) != 0:
    #         res2 += int(j) * (2 ** b)
    #     b -= 1
    # print(res2) 