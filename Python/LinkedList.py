# 
# Linked list | Python
# 

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        values = []
        current = self.head
        while current:
            values.append(repr(current.value))
            current = current.next
        return " -> ".join(values)


    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node


    def prepend(self, value):
        new_node = Node(value)
        new_node.next = self.head  
        self.head = new_node


    def insert_at(self, index, value):
        if index < 0:
            raise IndexError("Index must be non-negative")

        new_node = Node(value)

        if index == 0:
            self.prepend(value)
            return

        current = self.head
        count = 0

        while current and count < index - 1:
            current = current.next
            count += 1

        if current is None:
            raise IndexError("Index out of bounds")

        new_node.next = current.next
        current.next = new_node


    def delete_by_value(self, value):
        if self.head is None:
            return 

        if self.head.value == value:
            self.head = self.head.next
            return

        current = self.head
        while current.next and current.next.value != value:
            current = current.next

        if current.next:
            current.next = current.next.next


    def find(self, value):
        current = self.head
        index = 0
        while current:
            if current.value == value:
                return index
            current = current.next
            index += 1
        return -1
    

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev






