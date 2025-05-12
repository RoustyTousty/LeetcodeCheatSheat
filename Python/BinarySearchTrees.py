# 
# Binary Search Trees | Python
# 



class BSTNode:
    def __init__(self, value):
        self.value = value  
        self.left = None    
        self.right = None   


    #
    # Inserts a new BSTNode
    #
    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        elif value > self.value:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)


    #
    # Returns if the value is present in BST
    #
    def search(self, value):
        if value == self.value:
            return True
        elif value < self.value:
            return self.left.search(value) if self.left else False
        else:
            return self.right.search(value) if self.right else False
        

    #
    # Returns the last/peak element from the stack
    #
    def inorder_traversal(self):
        result = []
        if self.left:
            result += self.left.inorder_traversal()
        result.append(self.value)
        if self.right:
            result += self.right.inorder_traversal()
        return result


    #
    # Returns the height/debth of BST
    #
    def get_height(self):
        left_height = self.left.get_height() if self.left else 0
        right_height = self.right.get_height() if self.right else 0
        return 1 + max(left_height, right_height)


    #
    # Returns if the BST is balanced
    #
    def is_balanced(self):
        left_height = self.left.get_height() if self.left else 0
        right_height = self.right.get_height() if self.right else 0
        if abs(left_height - right_height) > 1:
            return False
        left_balanced = self.left.is_balanced() if self.left else True
        right_balanced = self.right.is_balanced() if self.right else True
        return left_balanced and right_balanced


    #
    # Deletes a value from BST
    #
    def delete(self, value):
        if value < self.value:
            if self.left:
                self.left = self.left.delete(value)
        elif value > self.value:
            if self.right:
                self.right = self.right.delete(value)
        else:
            if not self.left:
                return self.right
            if not self.right:
                return self.left

            min_larger_node = self.right
            while min_larger_node.left:
                min_larger_node = min_larger_node.left

            self.value = min_larger_node.value
            self.right = self.right.delete(min_larger_node.value)
        return self


    #
    # Visualizer
    #
    def print_tree(self, level=0, prefix="Root: "):
        if self.right:
            self.right.print_tree(level + 1, "R--- ")
        print("    " * level + prefix + str(self.value))
        if self.left:
            self.left.print_tree(level + 1, "L--- ")


# 
# Test scenarios
# 
# def test_bst():
#     print("Creating BST and inserting values...")
#     root = BSTNode(10)
#     root.insert(5)
#     root.insert(15)
#     root.insert(3)
#     root.insert(7)
#     root.insert(12)
#     root.insert(18)

#     print("\nBST structure:")
#     root.print_tree()

#     inorder = root.inorder_traversal()
#     expected_inorder = [3, 5, 7, 10, 12, 15, 18]
#     assert inorder == expected_inorder, f"Inorder traversal failed: expected {expected_inorder}, got {inorder}"
#     print("Inorder traversal test passed.")
    
#     assert root.search(7), "Search for 7 should return True"
#     print("Search for 7 passed.")
#     assert not root.search(99), "Search for 99 should return False"
#     print("Search for 99 passed.")

#     height = root.get_height()
#     assert height == 3, f"Tree height should be 3 but got {height}"
#     print(f"Height test passed. Height: {height}")

#     assert root.is_balanced(), "Tree should be balanced"
#     print("Balance check passed.")

#     print("\nDeleting node 5 (has two children)...")
#     root.delete(5)
#     new_inorder = root.inorder_traversal()
#     expected_after_delete = [3, 7, 10, 12, 15, 18]
#     assert new_inorder == expected_after_delete, f"Delete failed: expected {expected_after_delete}, got {new_inorder}"
#     print("Delete test passed.")

#     print("\nBST structure after deletion:")
#     root.print_tree()

#     print("\nAll BST tests passed!")
# test_bst()