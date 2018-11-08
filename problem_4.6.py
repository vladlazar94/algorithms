# Problem 4.6: Write an algorithm to find the "next" node (in-order succession)
# of a given node in a binary search tree. You may assume that each node has
# a link to its parent.

class BSTree:
    
    def __init__ (self, data = None):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None

    def insert (self, data):
        if self.data is None:
            self.data = data
        elif data < self.data:
            if self.left is None:
                self.left = BSTree(data)
                self.left.parent = self
            else:
                self.left.insert(data)
        elif data > self.data:
            if self.right is None:
                self.right = BSTree(data)
                self.right.parent = self
            else:
                self.right.insert(data)
        else:
            return
    
    def inorder_print (self):
        if self.left is not None:
            self.left.inorder_print()
        print(self.data)
        if self.right is not None:
            self.right.inorder_print()


def next(node):
    
    def lowest_left(node):
        if node.left is None:
            return node
        return lowest_left(node.left)

    def highest_right(node):
        if node.parent is None:
            return None
        if node is node.parent.left:
            return node.parent
        return highest_right(node.parent)
            
    if node.right is not None:
        return lowest_left(node.right)
    
    elif node.parent is not None:
        if node is node.parent.left:
            return node.parent
        else:
            return highest_right(node)
    else:
        return node
