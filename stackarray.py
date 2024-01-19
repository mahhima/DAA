class StackArray:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("pop from an empty stack")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("peek from an empty stack")

    def size(self):
        return len(self.items)


# Example Usage:
stack_array = StackArray()
stack_array.push(1)
stack_array.push(2)
stack_array.push(3)

print("Stack using Array:")
print("Peek:", stack_array.peek())
print("Pop:", stack_array.pop())
print("Size:", stack_array.size())
print("Is Empty:", stack_array.is_empty())
