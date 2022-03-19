# B. Список дел
# ---------------
# Васе нужно распечатать свой список дел на сегодня.
# Помогите ему: напишите функцию, которая печатает все его дела.

# 40ms | 3.97Mb


# Comment it before submitting
class Node:
    def __init__(self, value, next_item=None):
        self.value = value
        self.next_item = next_item

    def set_data(self, value):
        self.value = value

    # вернет то же самое, что и node.value
    def get_data(self):
        return self.value


def solution(node):
    while node != None:
        print(node.value, end="->")
        node = node.next_item
    print("None")


def get_node_by_index(node, index):
    while index:
        node = node.next_item
        index -= 1
    return node


def insert_node(head, index, value):
    new_node = Node(value)  # новый экземпляр класса Node
    if index == 0:
        new_node.next_item = head  # head - это текущий первый node0,
        # теперь он становится вторым элементом(node1) или следующим для нового элемента(new_node),
        # который мы поставили на первое место
        return new_node
    previous_node = get_node_by_index(head, index-1)
    new_node.next_item = previous_node.next_item
    previous_node.next_item = new_node
    return head


def main():
    node3 = Node("node3", None)
    node3.set_data('govno')

    node2 = Node("node2", node3)
    node2.set_data('jopa')

    node1 = Node("node1", node2)
    node0 = Node("node0", node1)
    solution(node0)
    print('ind: ', get_node_by_index(node0, 3))

    # node, index, value = node0, 1, 'new_node'
    # head = insert_node(node, index, value)
    # print('before')
    # solution(head)

    # Output is:
    # node0
    # node1
    # node2
    # node3


if __name__ == '__main__':
    main()
