# Problem 4.3: Given a binary tree, write an algorihm that 
# creates a linked list of all the nodes at each depth.

from collections import deque

# Using a binary search tree, without lack of generalization,
# as it is more convenient to initialize.
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

    def print_inorder (self):
        if self.left is not None:
            self.left.print_inorder()
        print(self.data)
        if self.right is not None:
            self.right.print_inorder()
        
    def list_of_depths_rec (self):
        list_of_depths = {}

        def inner (bstree, level):
            if bstree.left is not None:
                inner(bstree.left, level + 1)
            if level in list_of_depths:
                list_of_depths[level].append(bstree.data)
            else:
                list_of_depths[level] = deque()
                list_of_depths[level].append(bstree.data)
            if bstree.right is not None:
                inner(bstree.right, level + 1)

        inner(self, 0)
        return list_of_depths

    def list_of_depths_iter (self):   
        list_of_depths = {}
        q = deque()
        q.appendleft((self, 0))
        
        while len(q) is not 0:
            pair = q.pop()
            node = pair[0]
            level = pair[1]
            if level in list_of_depths:
                list_of_depths[level].append(node.data)
            else:
                list_of_depths[level] = deque()
                list_of_depths[level].append(node.data)
            if node.left is not None:
                q.appendleft((node.left, level + 1))
            if node.right is not None:
                q.appendleft((node.right, level + 1))
        
        return list_of_depths

            





