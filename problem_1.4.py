# Problem_4: Write a program that checks whether
# a given string is a permutation of a palindrome.


def palindrome_permutation (string):
    char_map = {}

    for char in string:
        if char in char_map:
            del char_map[char]
        else:
            char_map[char] = True

    if len(char_map) > 1:
        return False
    
    return True

