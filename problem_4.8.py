# Problem 4.8: Design an algorithm and write code to find 
# the first common ancestor of two nodes in a binary tree. 
# Avoid storing aditional nodes in a data structure.

class BTree:
    
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
                self.left = BTree(data)
                self.left.parent = self.left
            else:
                self.left.insert(data)
        elif data > self.data:
            if self.right is None:
                self.right = BTree(data)
                self.right.parent = self.right
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

    def contains_data (self, data):
        if self is None:
            return False
        if self.data is data:
            return True
        in_left = self.left.contains_data(data)
        in_right = self.right.contains_data(data)
        return in_left or in_right

    def upwards_search (self, data, search_left):
        if self is None or self.data is data:
            return self
        if search_left:
            in_subtree = self.left.contains_data(data)
        else:
            in_subtree = self.right.contains_data(data)
        if in_subtree:
            return self
        if self.parent.left.data is self.data:
            return self.parent.upwards_search(data, search_left = False)
        else:
            return self.parent.upwards_search(data, search_left = False)

    def common_ancestor_wlp (self, first, second):
        if first.contains_data(second.data):
            return first
        if first.parent.left.data is first.data:
            return first.parent.upwards_search(data = second.data, left = False)
        else:
            return first.parent.upwards_search(data = second.data, left = True)
            
        

            
            
        
        
        

