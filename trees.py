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
    
    def inorder_print (self):
        if self.left is not None:
            self.left.inorder_print()
        print(self.data)
        if self.right is not None:
            self.right.inorder_print()


