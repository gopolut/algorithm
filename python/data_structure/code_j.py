# J. Списочная очередь
# ------------------
# очередь, написанная с использованием связного списка.
# Помогите ему с реализацией.
# Очередь должна поддерживать выполнение трёх команд:
#  get() — вывести элемент, находящийся в голове очереди, и удалить его.
#         Если очередь пуста, то вывести «error».
#  put(x) — добавить число x в очередь
#  size() — вывести текущий размер очереди

# 52ms | 4.02Mb


class Node:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev

    def set_data(self, value):
        self.value = value

    # вернет то же самое, что и node.value
    def get_data(self):
        return self.value


class linkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def count_node(self):
        count = 0
        node = self.head
        node_list = []
        while node:
            node_list.append(node.value)
            count += 1
            node = node.next
        return count

    def show_node(self):
        node = self.head
        node_list = []
        while node:
            node_list.append(node.value)
            node = node.next
        return node_list

    def put(self, item):
        new_node = Node(item)
        if self.count_node() == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = None
            new_node.prev = None
            print(new_node.value)
        else:
            prev_node = self.tail
            prev_node.next = new_node
            new_node.prev = prev_node
            new_node.next = None
            self.tail = new_node
            print('new: ', new_node.value)
            print('prev: ', prev_node.value)
        print('queue: ', self.show_node())

    def get(self):
        if self.count_node() == 0:
            return 'error'
        if self.count_node() == 1:
            get_item = self.head
            self.head = None
            # self.head.prev = None
            # self.head.next = None
            print('get=1:', get_item.value)
        else:
            get_item = self.head
            self.head = self.head.next
            print('self.head.next: ', self.head)
            self.head.prev = None
            print('get=: ', get_item.value)

        return get_item.value


def main():
    l = linkedList()
    n = int(input())
    result = []

    for i in range(n):
        command = input().split()
        if command[0] == 'put':
            l.put(command[1])
        if command[0] == 'get':
            result.append(l.get())
        if command[0] == 'size':
            result.append(l.count_node())

    print('-----------')

    for i in result:
        print(i)

    print('-----------')


if __name__ == '__main__':
    main()
