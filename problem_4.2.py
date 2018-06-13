# Problem 4.2: Given a sorted (increasing order) array with unique integer elements,
# write an algorithm to create a binary search tree of minimal height.

class Node:
    def __init__ (self, data):
        self.data = data
        self.left = None
        self.right = None 
    
def insert_binary (root, data):
    if root.data is None:
        root.data = data
    elif data < root.data:
        if root.left is None:
            root.left = Node(data)
        else:
            insert_binary(root.left, data)
    elif data > root.data:
        if root.right is None:
            root.right = Node(data)
        else:
            insert_binary(root.right, data)
    else: return

def print_inorder (root):
    if root is not None:
        print_inorder(root.left)
        print(root.data) 
        print_inorder(root.right)

def create_bst_rec (bst, sorted_list, index_start, index_end):
    if index_end - index_start == 1:
        insert_binary(bst, sorted_list[index_start])
        insert_binary(bst, sorted_list[index_end])
    elif index_end == index_start:
        insert_binary(bst, sorted_list[index_start])
    else:
        index_middle = (index_start + index_end) / 2
        insert_binary(bst, sorted_list[index_middle])
        create_bst_rec(bst, sorted_list, index_start, index_middle - 1)
        create_bst_rec(bst, sorted_list, index_middle + 1, index_end)

def create_balanced_bst (sorted_list):
    bst = Node(None)
    create_bst_rec(bst, sorted_list, 0, len(sorted_list) - 1)
    return bst

