# Problem 4.4: Implement a function to check 
# whether a binary tree is balanced.

# Using a binary search tree, without loss 
# of generality, for convenience.
class BSTree:
    
    def __init__ (self, data = None):
        self.data = data
        self.left = None
        self.right = None

    def insert (self, data):
        if self.data is None:
            self.data = data
        elif data < self.data:
            if self.left is None:
                self.left = BSTree(data)
            else:
                self.left.insert(data)
        elif data > self.data:
            if self.right is None:
                self.right = BSTree(data)
            else:
                self.right.insert(data)
        else:
            return
    
    def inorder_print(self):
        if self.left is not None:
            self.left.inorder_print()
        print(self.data)
        if self.right is not None:
            self.right.inorder_print()

    def is_balanced(self):
        
        def inner(node):
            if node is None: 
                return 0
            left = inner(node.left)
            right = inner(node.right)
            if (left is False) or (right is False):
                return False                 
            if abs(left - right) < 2: 
                return max(left, right) + 1
            return False
            
        return False if inner(self) is False else True

