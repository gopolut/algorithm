from logging import exception
from typing import List

# B. Калькулятор
# --------------
# ID: 65845972

#  63ms | 4.02Mb


class Stack():
    def __init__(self) -> None:
        self.queue = []
        # self.operation_list = [] удалить

    # добавление в стек
    def push(self, item):
        return self.queue.append(int(item))

    # берем элемент с вершины стека и добавляем его в массив для операций
    def pop(self):
        if len(self.queue) != 0:
            return self.queue.pop()
        # return 'error'
        raise IndexError('Стек пуст!')

# =============================================================================
    # добавляем в список для проведения операций
    def push_operation(self, x):
        self.operation_list.append(x)

    # проводим операцию с операндами
    def calculate(self, operation):
        # добавляем в массив
        self.pop_append()

        # проводим операцию в зависимости от операнда: +, -, *, /
        # TODO: input_values = tuple(map(int, input_values))

        if operation == '+':
            result = sum(self.operation_list)
        elif operation == '-':
            result = self.operation_list[1] - self.operation_list[0]
        elif operation == '*':
            result = self.operation_list[1] * self.operation_list[0]
        elif operation == '/':
            result = self.operation_list[1] // self.operation_list[0]
        else:
            # TODO: какой exception
            raise exception('')

        # очищаем operation_list
        self.operation_list.clear()
        # добавляем в стек
        self.push(result)

    # элемент с вершины стека и добавляем его в массив для проведения операций
    def pop_append(self):
        counter = 0
        while counter < 2:
            x = self.queue.pop()
            # TODO:
            # first_operand = self.queue.pop()
            # second_operand = self.queue.pop()
            first_operand, second_operand = self.queue.pop(), self.queue.pop()
            self.push_operation(x)
            counter += 1



    # возвращает максимальное число в стеке;
    # def get_max(self):
    #     if len(self.queue) != 0:
    #         return max(self.queue)
    #     return None

    # def show(self):
    #     print('queue: ', self.queue)
    #     print('peration_list: ', self.operation_list)


def read_input() -> List[int]:
    numbers_sings = input()
    number_list = list(numbers_sings.strip().split())
    return number_list


def main():
    s = Stack()
    numbers_sings = read_input()
    sings = '+-*/'
    for i in numbers_sings:
        if i in sings:
            s.calculate(i)
        else:
            s.push(i)
        # s.show()
    print(s.pop())


if __name__ == '__main__':
    main()
