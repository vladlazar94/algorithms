class Node:
    def __init__(self, value=None):
        self.value = value
        self.right = None
        self.left = None


class Deque:

    def __init__(self):
        self.right_end = None
        self.left_end = None

    def push_right(self, value):
        if not (self.right_end or self.left_end):
            self.right_end = Node(value)
            self.left_end = self.right_end

        else:
            self.right_end.right = Node(value)
            self.right_end.right.left = self.right_end
            self.right_end = self.right_end.right

    def push_left(self, value):
        if not (self.right_end or self.left_end):
            self.right_end = Node(value)
            self.left_end = self.right_end

        else:
            self.left_end.left = Node(value)
            self.left_end.left.right = self.left_end
            self.left_end = self.left_end.left

    def pop_right(self):
        if self.right_end:
            self.right_end = self.right_end.left

    def pop_left(self):
        if self.left_end:
            self.left_end = self.left_end.right


