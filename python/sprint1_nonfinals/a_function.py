import collections

'''
https://contest.yandex.ru/contest/23389/problems/
A. Значения функции
'''

Function = collections.namedtuple('Function', ('parameter_a', 'number_x', 'parameter_b', 'parameter_c'))

def transform(input_list):
    nums = [int(x) for x in input_list]
    func = Function(nums[0], nums[1], nums[2], nums[3])
    return func

def evaluate_function(func) -> int:
    print(f'func: *{func}')
    y = func.parameter_a*(func.number_x*func.number_x) + func.parameter_b*func.number_x + func.parameter_c
    return y


if __name__ == '__main__':
    print(evaluate_function(transform(input().split())))
