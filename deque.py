class Node:
    def __init__(self, value=None):
        self.value = value
        self.right = None
        self.left = None


class Deque:

    def __init__(self, value=None):
        if value:
            self.right_end = Node(value)
            self.left_end = self.right_end
            self.size = 1
        else:
            self.right_end = None
            self.left_end = None
            self.size = 0

    def __len__(self):
        return self.size

    def __iter__(self):
        iterator = self.left_end
        while iterator:
            yield iterator.value
            iterator = iterator.right

    def __str__(self):
        return str(self.items())

    def items(self):
        return [item for item in self]

    def push_right(self, value):
        if not (self.right_end or self.left_end):
            self.right_end = Node(value)
            self.left_end = self.right_end

        else:
            self.right_end.right = Node(value)
            self.right_end.right.left = self.right_end
            self.right_end = self.right_end.right

        self.size += 1

    def push_left(self, value):
        if not (self.right_end or self.left_end):
            self.right_end = Node(value)
            self.left_end = self.right_end

        else:
            self.left_end.left = Node(value)
            self.left_end.left.right = self.left_end
            self.left_end = self.left_end.left

        self.size += 1

    def pop_right(self):
        if self.right_end:
            self.right_end = self.right_end.left
            self.size -= 1

    def pop_left(self):
        if self.left_end:
            self.left_end = self.left_end.right
            self.size -= 1

    def for_each(self, func):
        iterator = self.left_end
        while iterator:
            func(iterator.value)
            iterator = iterator.right

