# Problem 4.2: Given a sorted (increasing order) array with unique integer elements,
# write an algorithm to create a binary search tree of minimal height.

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
    
    def inorder_print (self):
        if self.left is not None:
            self.left.inorder_print()
        print(self.data)
        if self.right is not None:
            self.right.inorder_print()

def assemble_bst_rec  (sorted_list, index_start, index_end):
    if index_end < index_start:
        return None    
    index_middle = (index_start + index_end) // 2
    bst = BSTree(sorted_list[index_middle])
    bst.left = assemble_bst_rec(sorted_list, index_start, index_middle - 1)
    bst.right = assemble_bst_rec(sorted_list, index_middle + 1, index_end)
    return bst

def assemble_bst (sorted_list):
    return assemble_bst_rec(sorted_list, 0, len(sorted_list) - 1)



