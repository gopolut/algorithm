# D. Заботливая мама
# ------------------
# Мама Васи хочет знать, что сын планирует делать и когда. Помогите ей: напишите функцию solution,
# определяющую индекс первого вхождения передаваемого ей на вход значения в связном списке, если значение присутствует.

# 41ms | 4.50Mb


# Comment it before submitting
class Node:
    def __init__(self, value, next_item=None):
        self.value = value
        self.next_item = next_item


def get_node(node, elem):
    while node != None:
        if node.value == elem:
            return node
        node = node.next_item
    return None


def solution(node, elem):
    if get_node(node, elem) is None:
        return -1
    node_val = get_node(node, elem)
    count = 0
    while True:
        if node_val == node:
            return count
        node = node.next_item
        count += 1


def test():
    node4 = Node("node155", None)
    node3 = Node("node3", node4)
    node2 = Node("node2", node3)
    node1 = Node("node1", node2)
    node0 = Node("node0", node1)
    idx = solution(node0, "node155")
    print(idx)
    # result is idx == 2


if __name__ == '__main__':
    test()
