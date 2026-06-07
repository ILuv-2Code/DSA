class Node:
    def __init__(self, item, next=None):
        self.item = item
        self.next = next

class Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None