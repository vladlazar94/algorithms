# Problem 4.9: BST Sequences 
# A binary search tree was created by traversing an array 
# from left to right and inserting each element. Given a 
# binary tree with distinct elements, print all possible 
# arrays that could have led to this three.



def permutations (nums):
    
    if len(nums) is 0:
        return []
                
    perms = []

    for num in nums:
        
        others = permutations([oth for oth in nums if oth is not num])

        if len(others) is 0:
            perms.append([num])
        else:
            for other in others:
                perms.append([num] + other)

    return perms



def intertwine (first, second):
    
    if first and second:

        collect = []

        for index in range(len(second) + 1):
        
            slice = second[0:index]
            slice.append(first[0])

            others = intertwine(first[1:], second[index:])

            if len(others) is 0:
                collect.append(slice)
            else:
                for other in others:
                    collect.append(slice + other)

        return collect
            
    return [first + second]



class BSTree:



    def __init__ (self, data = None):
        self.data = data
        self.left = None
        self.right = None
    


    def insert(self, data):
        if self.data is None:
            self.data = data
            return

        if data > self.data:
            if self.right is None:
                self.right = BSTree(data) 
            else:
                self.right.insert(data)

        elif data < self.data:
            if self.left is None:
                self.left = BSTree(data) 
            else:
                self.left.insert(data)



    def inorder_print (self):
        if self.left is not None:
            self.left.inorder_print()

        print(self.data)
        
        if self.right is not None:
            self.right.inorder_print()



    def list_of_depths (self):
        depth_list = {}

        def inner (node, depth):
            if node is not None:
                inner(node.left, depth + 1)
                if depth not in depth_list:
                    depth_list[depth] = []
                depth_list[depth].append(node.data)
                inner(node.right, depth + 1)

        inner(self, 0)
        return depth_list

    

    def bst_sequences (self):

        collect = []

        if self.left is not None:
            left_seq = self.left.bst_sequences()
        else:
            left_seq = []
        if self.right is not None:
            right_seq = self.right.bst_sequences()
        else:
            right_seq = []

        if left_seq and right_seq:
            for lseq in left_seq:
                for rseq in right_seq:
                    for inter in intertwine(lseq, rseq):
                        collect.append(inter)
        else: 
            for lseq in left_seq:
                collect.append(lseq)
            for rseq in right_seq:
                collect.append(rseq)
        
        if collect:
            for seq in collect:
                seq.insert(0, self.data)     
            return collect

        return [[self.data]]



bst = BSTree(5)
bst.insert(3)
bst.insert(7)
bst.insert(1)
bst.insert(4)
bst_seq = bst.bst_sequences()
for seq in bst_seq:
    print(seq)

