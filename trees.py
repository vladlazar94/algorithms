class BinaryTreeNode:
    def __init__ (self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def get_left (self):
        return self.left

    def get_right (self):
        return self.right
    
    def get_data (self):
        return self.data

    def set_left (self, left):
        self.left = left

    def set_right (self, right):
        self.right = right

    def set_data (self, data):
        self.data = data

class BinarySearchTree:
    def __init__ (self):
        self.root = BinaryTreeNode(None)

    def set_root (self, root):
        self.root = root

    def get_root (self):
        return self.root

    def insert_rec (self, node, data):
        if data < node.get_data():
            if node.get_left() is None:
                node.set_left(BinaryTreeNode(data))
            else:
                self.insert_rec(node.get_left(), data)
        elif data > node.get_data():
            if node.get_right() is None: 
                node.set_right(BinaryTreeNode(data))
            else:
                self.insert_rec(node.get_right(), data)
        else: return

    def insert (self, data):
        if self.root.get_data() is None:
            self.root.set_data(data)
        else:
            self.insert_rec(self.root, data)

    def print_inorder_rec (self, node):
        if node is not None:
            self.print_inorder_rec(node.get_left())
            print(node.get_data())
            self.print_inorder_rec(node.get_right())

    def print_inorder (self):
        self.print_inorder_rec(self.root)

