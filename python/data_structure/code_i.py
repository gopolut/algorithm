# I. Ограниченная очередь
# -----------------------
# Тимофею нужно написать класс MyQueueSized, который принимает параметр max_size,
# означающий максимально допустимое количество элементов в очереди.

# 51ms | 3.97Mb


class MyQueueSized():
    def __init__(self, max_size) -> None:
        self.queue = []
        self.max_size = max_size

    # Добавление числа в очередь
    def push(self, item):
        if self.size() + 1 > self.max_size:
            return 'error'
        self.queue.append(item)

    # Удаление первого числа из очереди
    def pop(self):
        if self.size() == 0:
            return None
        # сохраняем число
        last_number = self.queue[0]
        # удаляем
        self.queue.pop(0)
        return last_number

    # первое число из очереди
    def peek(self):
        if self.size() == 0:
            return None
        return self.queue[0]

    # размер очереди
    def size(self):
        q_length = len(self.queue)
        return q_length


def main():
    n = int(input())
    size = int(input())
    q = MyQueueSized(size)
    result = []

    for i in range(n):
        command = input().split()
        if command[0] == 'push':
            if q.push(command[1]) == 'error':
                result.append('error')
        if command[0] == 'pop':
            result.append(q.pop())
        if command[0] == 'size':
            result.append(q.size())
        if command[0] == 'peek':
            result.append(q.peek())

    print('-----------')

    for i in result:
        print(i)


if __name__ == '__main__':
    main()
