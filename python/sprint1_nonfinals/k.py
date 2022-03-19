from typing import List, Tuple
'''
K. Списочная форма
'''

# 64ms | 3.98Mb

def get_sum(number_list: List[int], k: int) -> List[int]:
    nums = int(''.join(map(str, number_list)))
    print('nums: ', nums + k)
    a = str(nums + k)
    print('a: ', a)
    return a

def read_input() -> Tuple[List[int], int]:
    n = int(input())
    number_list = list(map(int, input().strip().split()))
    k = int(input())
    return number_list, k

number_list, k = read_input()
print(' '.join(map(str, get_sum(number_list, k))))
