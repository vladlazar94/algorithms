# Problem 4.5: Implement a function that checks 
# if a binary tree is a binary search tree.

class BTree:
    
    def __init__ (self, data = None):
        self.data = data
        self.left = None
        self.right = None

    def inorder_print (self):
        if self.left is not None:
            self.left.inorder_print()
        print(self.data)
        if self.right is not None:
            self.right.inorder_print()

    def is_bst (self):
    
        def inner (node, minimum, maximum):   
            if node is None:
                return True
            if node.data < minimum or node.data > maximum:
                return False
            return inner(node.left, minimum, node.data) and inner(node.right, node.data, maximum)

        return inner(self, float('-inf'), float('inf'))
    
