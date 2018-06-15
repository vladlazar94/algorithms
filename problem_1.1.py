# Problem 1.1: Write a program that detects whether a string has all unique characters.

def unique_chars (string):
    
    char_map = {}

    for char in string:
        if char in char_map:
            return False
        char_map[char] = True
    
    return True

