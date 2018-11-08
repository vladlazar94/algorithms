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


