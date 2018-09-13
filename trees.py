from deque import Deque


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

    def in_order_search(self, func=print):

        if self.left is not None:
            self.left.in_order_search()

        func(self.value)

        if self.right is not None:
            self.right.in_order_search()

    def list_of_depths(self):
        depths = {}

        def collect(node, depth):
            if depth in depths:
                depths[depth].push_right(node.value)
            else:
                depths[depth] = Deque(node.value)

            if node.left:
                collect(node.left, depth + 1)
            if node.right:
                collect(node.right, depth + 1)

        collect(self, 0)
        return depths








