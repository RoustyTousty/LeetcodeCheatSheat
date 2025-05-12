# 
# Linked list | Python
# 


# Linked lists node class
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


# Main linked list manager class
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



    #
    # Adds a new value to the end
    #
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node


    #
    # Adds a new value to the start
    #
    def prepend(self, value):
        new_node = Node(value)
        new_node.next = self.head  
        self.head = new_node


    #
    # Inserts a new value at index position
    #
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


    #
    # Deletes a node by its value
    #
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


    #
    # Finds a node by its value
    #
    def find(self, value):
        current = self.head
        index = 0
        while current:
            if current.value == value:
                return index
            current = current.next
            index += 1
        return -1
    

    #
    # Reverses the linked list
    #
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev
        
        
        
# 
# Test scenarios
# 
# def test_linked_list():
#     print("Testing LinkedList:")

#     ll = LinkedList()


#     ll.append(1)
#     ll.append(2)
#     ll.append(3)
#     print("After append:", ll) 


#     ll.prepend(0)
#     print("After prepend:", ll)


#     ll.insert_at(2, 1.5)
#     print("After insert at index 2:", ll) 


#     print("Index of 1.5:", ll.find(1.5)) 
#     print("Index of 99:", ll.find(99))  


#     ll.delete_by_value(1.5)
#     print("After deleting 1.5:", ll) 


#     ll.reverse()
#     print("After reverse:", ll) 
# test_linked_list()