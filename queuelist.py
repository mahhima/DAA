class QueueNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class QueueLinkedList:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, item):
        new_node = QueueNode(item)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if not self.is_empty():
            removed = self.front.data
            self.front = self.front.next
            if self.front is None:
                self.rear = None
            return removed
        else:
            raise IndexError("dequeue from an empty queue")

    def front_element(self):
        if not self.is_empty():
            return self.front.data
        else:
            raise IndexError("front from an empty queue")

    def size(self):
        current = self.front
        count = 0
        while current:
            count += 1
            current = current.next
        return count


# Example Usage:
queue_linked_list = QueueLinkedList()
queue_linked_list.enqueue(1)
queue_linked_list.enqueue(2)
queue_linked_list.enqueue(3)

print("\nQueue using Linked List:")
print("Front:", queue_linked_list.front_element())
print("Dequeue:", queue_linked_list.dequeue())
print("Size:", queue_linked_list.size())
print("Is Empty:", queue_linked_list.is_empty())
