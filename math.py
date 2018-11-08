def combinations(data, size):
    if size is 1:
        return [[element] for element in data]

    combs = []
    for i in range(len(data)):
        others = combinations(data[i + 1:], size - 1)
        combs += [[data[i]] + other for other in others]

    return combs


def permutations(data):
    if len(data) is 1:
        return [data]

    perms = []

    for i in range(len(data)):
        others = permutations(data[0: i] + data[i+1:])
        for perm in others:
            perm.append(data[i])
        perms += others

    return perms


def arrangements(data, size):
    arrs = []
    for comb in combinations(data, size):
        arrs += permutations(comb)

    return arrs

