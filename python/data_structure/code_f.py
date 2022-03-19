# F. Стек - Max
# -------------
# Нужно реализовать класс StackMax, который поддерживает операцию определения максимума среди всех элементов в стеке.
# Класс должен поддерживать операции:
#  push(x), где x – целое число,
#  pop()
#  get_max()

# 85ms | 4.06Mb

class Steck():
    def __init__(self) -> None:
        self.lst = []

    # добавление в стек
    def push(self, item):
        return self.lst.append(int(item))

    # возвращает элемент с вершины стека и удаляет его
    def pop(self):
        if len(self.lst) != 0:
            return self.lst.pop()
        return 'error'

    # возвращает максимальное число в стеке;
    def get_max(self):
        if len(self.lst) != 0:
            return max(self.lst)
        return None

    def show(self):
        print(self.lst)


def main():
    s = Steck()
    n = int(input())
    result = []

    for i in range(n):
        command = input().split()
        if command[0] == 'push':
            s.push(command[1])
        if command[0] == 'pop':
            if s.pop() == 'error':
                result.append('error')
        if command[0] == 'get_max':
            result.append(s.get_max())

    for i in result:
        print(i)

    print('-----------')
    s.show()

# def main():
#     s1 = Steck()
#     # s1.push(33)
#     # s1.push(44)
#     # s1.push(51)

#     print(s1.get_max())
#     print(s1.pop())


if __name__ == '__main__':
    main()
