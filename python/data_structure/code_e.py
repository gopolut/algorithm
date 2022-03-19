# Comment it before submitting
class DoubleConnectedNode:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev


def count_node(node):
    node_list = []
    count = 0
    while node:
        count += 1
        node_list.append(node)
        node = node.next
    print(node_list)
    print(count)
    return node_list


def solution(node):
    p = node.next
    n = node

    node.next = None
    node.prev = node.next

    while p is not None:
        p.prev = p.next
        p.next = n  # следующий элемент равен предыдущему
        n = p  # итератор для предыдущего элемента = текущему элементу
        p = p.prev  # итератор, получаем след. элемент: p.prev = p.next
    node = n
    # return node

    while node:
        print(node.value, end="->")
        node = node.next
    print("None")

# def solution(node):
#     lst_node = count_node(node)
#     for i in range(0, len(lst_node)):
#         if i == 0:
#             lst_node[i].prev = lst_node[i + 1]
#             lst_node[i].next = None
#             print(' ', lst_node[i].value)
#         elif i == len(lst_node)-1:
#             lst_node[i].prev = None
#             lst_node[i].next = lst_node[i - 1]
#             print(' ', lst_node[i].value)
# #             return lst_node[i]
#             node = lst_node[i]
#         else:
#             lst_node[i].prev = lst_node[i + 1]
#             lst_node[i].next = lst_node[i - 1]
#             print(' ', lst_node[i].value)

#     while node:
#         print(node.value, end="->")
#         node = node.next
#     print("None")


# def solution(node):
#     n = node
#     m = n.next
#     n.next = None
#     n.prev = m
#     while m is not None:
#         m.prev = m.next
#         m.next = n
#         n = m
#         m = m.prev
#     node = n
#     return node

#     while node:
#         print(node.value, end="->")
#         node = node.next
#     print("None")


def test():
    node3 = DoubleConnectedNode("node3")
    node2 = DoubleConnectedNode("node2")
    node1 = DoubleConnectedNode("node1")
    node0 = DoubleConnectedNode("node0")

    node0.next = node1

    node1.prev = node0
    node1.next = node2

    node2.prev = node1
    node2.next = node3

    node3.prev = node2
    new_head = solution(node0)
    # result is new_head == node3
    # node3.next == node2
    # node2.next == node1 node2.prev == node3
    # node1.next == node0 node1.prev == node2
    # node0.prev == node1


if __name__ == '__main__':
    test()
