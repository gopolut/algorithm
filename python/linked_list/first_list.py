
# Однонаправленный связанный список
from platform import node


class Node:
    def __init__(self, value=None, next=None) -> None:
        self.value = value
        self.next = next

    def set_data(self, value):
        self.value = value
    
    def show(self):
        if self.value == '':
            return 'This is delimiter' 
        return self.value


# выводит на печать все ячейки связанного списка
# top - указатель на первую ячейку
def iterate(top):
    while top != None:
        print(top.value)
        top = top.next  # для перехода к следующей ячейке
    print(None)

# находит ячейку по значению
def find_node_by_value(top, target):
    while top:
        if top.value == target:
            return top, top.show()
        top = top.next  # для перехода к следующей ячейке
    return None

# Находит ячейку по значению, предшествующую целевой
def find_before(top, target):
    # if top == None:
    #     return None
    while top.next:
        if top.next.value == target:
            return top
        top = top.next
    return None

# Добавление в начало списка
def add_begin(top, new_node):
    new_node.next = top.next
    top.next = new_node

# Добавление в конец списка
def add_end(top, new_node):
    while top.next:
        top = top.next
    
    new_node.next = None
    top.next = new_node

# Находит предыдущую ячейку
def find_prev_node(top, target_node):
    while top.next:
        if top.next == target_node:
            return top
        top = top.next
    return None


# Удаление ячейки
def delete_node(top, deleted_node):
    after_me = find_prev_node(top, deleted_node)
    after_me.next = deleted_node.next


if __name__ == '__main__':
    node4 = Node(23459)
    node3 = Node('govno', node4)
    node2 = Node('sraka', node3)
    node1 = Node('jopa', node2)
    node0 = Node('', node1)  # ограничитель

    iterate(node1)
    # print(find_node_by_value(node1, 'jopa'))
    # print(find_before(node0, 'jopa').show())
    print('---------------')

    node_new = Node('new_val')
    add_begin(node0, node_new)
    iterate(node0)

    print('---------------')
    print(' Вставили в конец')

    ended_node = Node('end-point')
    add_end(node0, ended_node)
    iterate(node0)

    print('---------------')
    delete_node(node0, node4)
    print(' Удалили node4 with value 23459')
    iterate(node0)
