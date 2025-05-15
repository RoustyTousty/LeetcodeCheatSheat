# 
# Stacks & Queues | Python
# 


# Stack manager class
class Stack:
    def __init__(self):
        self.items = []


    #
    # Adds/Creates a new value in the stack
    #
    def push(self, value):
        self.items.append(value)


    #
    # Removes last element from the stack
    #
    def pop(self):
        return self.items.pop()


    #
    # Returns the last/peak element from the stack
    #
    def peek(self):
        return self.items[-1]


    #
    # Returns if the stack is empty or not
    #
    def is_empty(self):
        return len(self.items) == 0




# Queue manager class
class Queue:
    def __init__(self):
        self.items = []


    #
    # Adds/Creates a new value in the queue
    #
    def enqueue(self, value):
        self.items.append(value)


    #
    # Removes an item from the queue
    #
    def dequeue(self):
        return self.items.pop(0)


    #
    # Returns the last/peak element from the stack
    #
    def peek(self):
        return self.items[0]


    #
    # Returns if the stack is empty or not
    #
    def is_empty(self):
        return len(self.items) == 0


# 
# Test scenarios
# 
# def test_stack_and_queue():
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
# test_stack_and_queue()