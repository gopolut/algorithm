# C. Нелюбимое дело
# -----------------
# Вася размышляет, что ему можно не делать из того списка дел, который он составил.
# Но, кажется, все пункты очень важные! Вася решает загадать число и удалить дело, которое идёт под этим номером. 

# 25ms | 3.46Mb


# Comment it before submitting
class Node:
    def __init__(self, value, next_item=None):
        self.value = value
        self.next_item = next_item


def get_node_by_index(node, index):
    while index:
        node = node.next_item
        index -= 1
    return node


def solution(node, idx):
    if idx == 0:
        node = node.next_item
    else:
        prev_node = get_node_by_index(node, idx - 1)
        cur_node = get_node_by_index(node, idx)

        prev_node.next_item = cur_node.next_item

    while node:
        print(node.value, end="->")
        node = node.next_item
    print("None")


def main():
    node3 = Node("node3", None)
    node2 = Node("node2", node3)
    node1 = Node("node1", node2)
    node0 = Node("node0", node1)
    new_head = solution(node0, 2)
    print('  ', new_head)
    # result is node0 -> node2 -> node3


if __name__ == '__main__':
    main()
