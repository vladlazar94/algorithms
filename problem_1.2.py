# Problem_2: Write a program that checks whether
# two strings are perumations of eachother.

def are_permutations (first, second):
    if len(first) is not len(second):
        return False

    char_map = {}

    for char in first:
        if char in char_map:
            char_map[char] += 1
        else:
            char_map[char] = 1

    for char in second:
        if char in char_map:
            char_map[char] -= 1
            if char_map[char] < 0:
                return False
        else: 
            return False
    
    return True

