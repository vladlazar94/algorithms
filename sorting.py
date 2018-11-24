def partition(container, lower_index, higher_index):
    if higher_index <= lower_index:
        return
    bound = lower_index - 1

    for i in range(lower_index, higher_index + 1):
        if container[i] <= container[higher_index]:
            aux = container[bound + 1]
            container[bound + 1] = container[i]
            container[i] = aux
            bound += 1

    partition(container, lower_index, bound - 1)
    partition(container, bound + 1, higher_index)


def quicksort(container):
    partition(container, 0, len(container) - 1)


class BinaryHeap:
    def __init__(self, array):
        self.inner_array = array
        self.heap_length = len(array)

    def current_level(self, index):
        if index >= self.heap_length:
            return None

        total, exponent = 0, 0
        while total <= index:
            total += 2 ** exponent
            exponent += 1

        return exponent - 1

    def left_index(self, index):
        pass

    def right_index(self, index):
        pass
