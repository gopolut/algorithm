# G. Стек - MaxEffective
# ----------------------
# Реализуйте класс StackMaxEffective, поддерживающий операцию определения максимума среди элементов в стеке.
# Сложность операции должна быть O(1).
# Для пустого стека операция должна возвращать None. 
# При этом push(x) и pop() также должны выполняться за константное время

# 439ms | 4.89Mb

class Steck():
    def __init__(self) -> None:
        self.lst = []
        self.max_list = []

    # добавление в стек
    def push(self, item):
        if len(self.lst) == 0:
            self.max_list.append(int(item))
        else:
            if int(item) >= self.max_list[-1]:
                self.max_list.append(int(item))  # вставляем в конец
        return self.lst.append(int(item))

    # возвращает элемент с вершины стека и удаляет его
    def pop(self):
        self.show()
        self.show_max()
        if len(self.lst) != 0:
            # d = len(self.lst)-1
            d = self.lst[-1]
            if d == self.max_list[-1]:
                self.max_list.pop()
            return self.lst.pop()
        return 'error'

    # находит максимум
    def get_max(self):
        if len(self.lst) != 0:
            return self.max_list[-1]
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

    print('-----------')

    for i in result:
        print(i)

    print('-----------')
    s.show()
    s.show_max()


if __name__ == '__main__':
    main()
