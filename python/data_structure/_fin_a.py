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

class Deque:
    def __init__(self, deque_size):
        self.elements = [None] * deque_size
        self.max_number = deque_size
        self.head = 0
        # self.head = deque_size
        self.tail = self.head
        self.size = 0

    def is_empty(self):
        return self.size == 0

    # добавление элемента в конец дека
    def push_back(self, value):
        if self.size == self.max_number:
            raise IndexError('Дек полностью заполнен!')
        self.tail = (self.tail + 1) % self.max_number
        self.elements[self.tail - 1] = value  # <--
        self.size += 1

    # добавление элемента в начало дека
    def push_front(self, value):
        if self.size == self.max_number:
            raise IndexError('Дек полностью заполнен!')
        self.head = (self.head - 1) % self.max_number  # <--
        self.elements[self.head] = value
        self.size += 1

    # вывод последнего значения (добавленный ранее всех элемент)
    def pop_back(self):
        if self.is_empty():
            raise IndexError('Дек пуст!')
        self.tail = (self.tail - 1) % self.max_number
        value = self.elements[self.tail]
        self.size -= 1
        return value

    # вывод первого элемента (добавленный последним)
    def pop_front(self):
        if self.is_empty():
            raise IndexError('Дек пуст!')
        self.head = (self.head + 1) % self.max_number
        value = self.elements[self.head - 1]
        self.size -= 1
        return value


if __name__ == '__main__':
    # main()


# def main():
    # command_count = int(input())
    # deck_size = int(input())
    # my_deck = Deck(deck_size)
    # result = []

    # for i in range(command_count):
    #     command = input().split()
    #     if command[0] == 'push_front':
    #         if my_deck.push_front(command[1]) == 'error':
    #             result.append('error')
    #     if command[0] == 'push_back':
    #         if my_deck.push_back(command[1]) == 'error':
    #             result.append('error')
    #     if command[0] == 'pop_front':
    #         result.append(my_deck.pop_front())
    #     if command[0] == 'pop_back':
    #         result.append(my_deck.pop_back())

    # print('-----------')
    # for i in result:
    #     print(i)
    # print('-----------').

    output = []
    command_count = int(input())
    deque = Deque(int(input()))

    for _ in range(command_count):
        command_name, *input_values = input().split()
        # object_value = getattr(my_deque, command_name)
        # input_values = tuple(map(int, input_values))
        # command = input().split()
        try:
            # result = object_value(*input_values)
            result = getattr(deque, command_name)(*input_values)
        except (IndexError, OverflowError):
            result = 'error'
        if result is not None:
            output.append(result)

    print(*output, sep='\n')
