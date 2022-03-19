import operator

# B. Калькулятор
# --------------
# ID: 65944448 (11 мар 2022, 19:02:26)
# ID: 65951364 (11 мар 2022, 23:17:07)

#  63ms | 4.02Mb


class Stack():
    def __init__(self) -> None:
        self.elements = []

    def push(self, item):
        return self.elements.append(item)

    def pop(self):
        try:
            return self.elements.pop()
        except IndexError:
            raise IndexError('Стек пуст!')

# OPERATIONS = {
#     '+': lambda first, second: operator.add(first, second),
#     '-': lambda first, second: operator.sub(first, second),
#     '*': lambda first, second: operator.mul(first, second),
#     '/': lambda first, second: operator.floordiv(first, second),
#     }


OPERATIONS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.floordiv,
    }


def calculator(symbols, stack=None, digitizer=int, operations=OPERATIONS):
    stack = Stack() if stack is None else stack
    for element in symbols:
        if element in operations:
            first, second = stack.pop(), stack.pop()
            stack.push(operations[element](second, first))
        else:
            try:
                stack.push(digitizer(element))
            except ValueError:
                raise ValueError(f'Символ "{element}" не является числом!')
    return stack.pop()


if __name__ == '__main__':
    print(calculator(input().split()))
