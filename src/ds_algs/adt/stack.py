class Stack:
    """List-backed stack implementation. Supports O(1) push and pop operations."""

    def __init__(self, items=None):
        self._L = list(items) if items is not None else []
    
    def peek(self):
        if not self._L:
            raise IndexError("can't peek empty stack")
        return self._L[-1]
    
    def __len__(self):
        return len(self._L)
    
    def push(self, item):
        self._L.append(item)
    
    def pop(self):
        if not self._L:
            raise IndexError("can't pop empty stack")
        return self._L.pop()