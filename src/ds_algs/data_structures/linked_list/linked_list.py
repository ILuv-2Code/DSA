class node:
    def __init__(self, data, link=None):
        self.data = data
        self.link = link

class linked_list:
    def __init__(self, items=None):
        self._head = None
        self._tail = None
        self._len = 0
    
        if items:
            for item in items:
                self.add_last(item)

    def __iter__(self):
        current = self._head

        while current is not None:
            yield current.data
            current = current.link

    def __len__(self):
        return self._len

    def add_first(self, item):
        if self._head is None:
            self._head = self._tail = node(item)
        else: 
            self._head = node(item, self._head)
        self._len += 1

    def add_last(self, item):
        if self._head is None and self._tail is None:
            self._head = self._tail = node(item)
        else:
            self._tail.link = node(item)
            self._tail = self._tail.link
        
        self._len += 1

    def remove_first(self):
        if self._head is None:
            raise IndexError("can't remove from an empty linked_list")
        else:
            self._head = self._head.link

            if self._head is None:
                self._tail = None
        
        self._len -= 1 

    def remove_last(self):
        if self._head is None:
            raise IndexError("can't remove from an empty linked_list")
            
        if self._head is self._tail:
            self._head = self._tail = None
        else:
            current = self._head
            while current.link is not self._tail:
                current = current.link

            current.link = None
            self._tail = current

        self._len -= 1