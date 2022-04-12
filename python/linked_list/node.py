
# Класс Node

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
