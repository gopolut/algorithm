# Однонаправленный связанный список
class LinkedList():
    def __init__(self) -> None:
        self.top = None

    # выводит на печать все ячейки связанного списка
    # top - указатель на первую ячейку
    def iterate(self, top):
        while top != None:
            print(top.value)
            top = top.next  # для перехода к следующей ячейке
        print(None)

    # находит ячейку по значению
    def find_node_by_value(self, top, target):
        while top:
            if top.value == target:
                return top, top.show()
            top = top.next  # для перехода к следующей ячейке
        return None

    # Находит ячейку по значению, предшествующую целевой
    def find_before(self, top, target):
        # if top == None:
        #     return None
        while top.next:
            if top.next.value == target:
                return top
            top = top.next
        return None

    # Добавление в начало списка
    def add_begin(self, top, new_node):
        new_node.next = top.next
        top.next = new_node

    # Добавление в конец списка
    def add_end(self, top, new_node):
        while top.next:
            top = top.next
        
        new_node.next = None
        top.next = new_node

    # Находит предыдущую ячейку
    def find_prev_node(self, top, target_node):
        while top.next:
            if top.next == target_node:
                return top
            top = top.next
        return None

    # Удаление ячейки
    def delete_node(self, top, deleted_node):
        after_me = self.find_prev_node(top, deleted_node)
        after_me.next = deleted_node.next
