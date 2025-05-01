# 
# Stacks & Queues | Python
# 

class Stack:
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    # pop
    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from empty stack")
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0


class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, value):
        self.items.append(value)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        return self.items.pop(0)

    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from empty queue")
        return self.items[0]

    def is_empty(self):
        return len(self.items) == 0



# if __name__ == "__main__":
#     # Test Stack
#     print("Testing Stack:")
#     s = Stack()
#     try:
#         s.pop()
#     except IndexError as e:
#         print(f"Caught error: {e}")

#     s.push(1)
#     s.push(2)
#     print("Top element:", s.peek())
#     print("Popped element:", s.pop())
#     print("Is stack empty?", s.is_empty())

#     # Test Queue
#     print("\nTesting Queue:")
#     q = Queue()
#     try:
#         q.dequeue()
#     except IndexError as e:
#         print(f"Caught error: {e}")

#     q.enqueue('a')
#     q.enqueue('b')
#     print("Front element:", q.peek())
#     print("Dequeued element:", q.dequeue())
#     print("Is queue empty?", q.is_empty())