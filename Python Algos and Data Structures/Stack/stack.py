# Stack follows FILO (First In, Last Out)
# Imagine a pile of books to replicate the stack data structure

# Push - insert element at the "top" of the stack
# Pop - remove element at the "top" position
# Peek - returns the "top" element of the stack

# All are basic operations of stack except get_stack

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def get_stack(self):
        return self.items
