class QueueArray:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("dequeue from an empty queue")

    def front(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("front from an empty queue")

    def size(self):
        return len(self.items)


# Example Usage:
queue_array = QueueArray()
queue_array.enqueue(1)
queue_array.enqueue(2)
queue_array.enqueue(3)

print("\nQueue using Array:")
print("Front:", queue_array.front())
print("Dequeue:", queue_array.dequeue())
print("Size:", queue_array.size())
print("Is Empty:", queue_array.is_empty())
