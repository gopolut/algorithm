from node import Node
from linked_list import LinkedList


if __name__ == '__main__':
    node4 = Node(23459)
    node3 = Node('govno', node4)
    node2 = Node('sraka', node3)
    node1 = Node('jopa', node2)
    node0 = Node('', node1)  # ограничитель

    first_list = LinkedList()
    first_list.iterate(node1)
    # print(find_node_by_value(node1, 'jopa'))
    # print(find_before(node0, 'jopa').show())
    print('---------------')

    node_new = Node('new_val')
    first_list.add_begin(node0, node_new)
    first_list.iterate(node0)

    print('---------------')
    print(' Вставили в конец')

    ended_node = Node('end-point')
    first_list.add_end(node0, ended_node)
    first_list.iterate(node0)

    print('---------------')
    first_list.delete_node(node0, node4)
    print(' Удалили node4 with value 23459')
    first_list.iterate(node0)