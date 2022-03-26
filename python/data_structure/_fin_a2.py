# A. Дек
# ------
# Гоша реализовал структуру данных Дек, максимальный размер которого определяется заданным числом.
# Методы push_back(x), push_front(x), pop_back(), pop_front() работали корректно.

# push_back(value) – добавить элемент в конец дека.
#              Если в деке уже находится максимальное число элементов, вывести «error».
# push_front(vaalue) – добавить элемент в начало дека.
#              Если в деке уже находится максимальное число элементов, вывести «error».
# pop_front() – вывести первый элемент дека и удалить его.
#              Если дек был пуст, то вывести «error».
# pop_back() – вывести последний элемент дека и удалить его.
#              Если дек был пуст, то вывести «error».

# 0.507s | 5.97Mb
# ID: 65948686 (11 мар 2022, 21:06:56)
# ID: 65953195 (12 мар 2022, 01:30:13)


class Deque:
    def __init__(self, deque_size):
        self.elements = [None] * deque_size
        self.max_number = deque_size
        self.head = 0
        self.tail = -1
        self.size = 0

    def is_empty(self):
        return self.size == 0

    # добавление элемента в конец дека
    def push_back(self, value):
        if self.size == self.max_number:
            raise IndexError('Дек полностью заполнен!')
        self.tail = (self.tail + 1) % self.max_number
        self.elements[self.tail] = value
        self.size += 1

    # добавление элемента в начало дека
    def push_front(self, value):
        if self.size == self.max_number:
            raise IndexError('Дек полностью заполнен!')
        self.head = (self.head - 1) % self.max_number
        self.elements[self.head] = value
        self.size += 1

    # вывод последнего значения (добавленный ранее всех элемент)
    def pop_back(self):
        if self.is_empty():
            raise IndexError('Дек пуст!')
        value = self.elements[self.tail]
        self.tail = (self.tail - 1) % self.max_number
        self.size -= 1
        return value

    # вывод первого элемента (добавленный последним)
    def pop_front(self):
        if self.is_empty():
            raise IndexError('Дек пуст!')
        value = self.elements[self.head]
        self.head = (self.head + 1) % self.max_number
        self.size -= 1
        return value


if __name__ == '__main__':
    output = []
    command_count = int(input())
    deque = Deque(int(input()))

    for _ in range(command_count):
        command, *input_values = input().split()
        try:
            result = getattr(
                deque,
                command,
                )(*input_values)
        except AttributeError:
            raise AttributeError(f'Команда "{command}" не поддерживается!')
        except IndexError:
            result = 'error'
        if result is not None:
            output.append(result)

    print(*output, sep='\n')
