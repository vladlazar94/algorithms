class BSTree:

    def __init__(self, value):

        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):

        if value > self.value:
            if self.right is None:
                self.right = BSTree(value)
            else:
                self.right.insert(value)
        
        if value < self.value:
            if self.left is None:
                self.left = BSTree(value)
            else:
                self.left.insert(value)

    def in_order_print(self):

        if self.left is not None:
            self.left.inorder_print()
        
        print(self.value)

        if self.right is not None:
            self.right.inorder_print()


tree = BSTree(5)
tree.insert(2)
tree.insert(6)
tree.insert(7)
tree.insert(1)

