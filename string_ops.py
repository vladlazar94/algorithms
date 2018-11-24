def urlfy(string):
    """ Replaces the emtpy spaces between words
        of a string with %20. """
    if len(string) is 0:
        return ""

    output = ""
    flag = False

    for char in string:    
        if char is not " ":
            output += char
            flag = True

        elif flag is True: 
            output += "%20"
            flag = False

    output = output[0: len(output) - 2]
    return output


def palindrome_permutation(string):
    """ Checks whether a given string is a
        permutation of a palindrome. """
    char_map = {}

    for char in string:
        if char in char_map:
            del char_map[char]
        else:
            char_map[char] = True

    if len(char_map) > 1:
        return False

    return True


def compress_string(string):
    """ Performs a basic string compression using the count of repeated
        characters. If the resulting string is not shorter, the initial
        string will be returned. """
    if len(string) < 2:
        return string

    indices = [0]
    for index in range (1, len(string)):
        if string[index] is not string[index - 1]:
            indices.append(index)
    indices.append(len(string))

    output = ""
    for index in range(0, len(indices) - 1):
        output += string[indices[index]]
        count = indices[index + 1] - indices[index]
        if count > 1:
            output += str(count)

    if len(output) > len(string):
        return string

    return output


def are_permutations(first, second):
    """ Checks whether two strings are
        permutations of each other. """
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


def longest_unique_substring(string):
    """ Finds the length of the longest substring
        without repeated characters. """
    char_map = {}

    checkpoint = -1
    longest_length = 0

    for index in range(0, len(string)):
        current_char = string[index]

        if current_char in char_map:
            if char_map[current_char] > checkpoint:

                current_length = index - checkpoint - 1
                checkpoint = char_map[current_char]

                if current_length > longest_length:
                    longest_length = current_length

        char_map[current_char] = index

    if longest_length is 0:
        return len(string)

    elif len(string) - checkpoint - 1 > longest_length:
        longest_length = len(string) - checkpoint - 1

    return longest_length


def one_edit_away(first, second):
    """ Checks whether two given strings are one edit away from each other.
        Edits include inserting, removing or replacing a character. """
    if abs(len(first) - len(second)) > 1:
        return False

    one_already = False
    if len(first) is len(second):
        for (first_char, second_char) in (first, second):
            if first_char is not second_char:
                if one_already:
                    return False
                one_already = True
        return True

    else:
        longer = first if len(first) > len(second) else second
        shorter = first if len(first) < len(second) else second

        longer_index = 0;
        shorter_index = 0;

        while shorter_index < len(shorter) and longer_index < len(longer):
            if shorter[shorter_index] is not longer[longer_index]:
                longer_index += 1
                if shorter[shorter_index] is not longer[longer_index]:
                    return False
                if longer_index - shorter_index > 1:
                    return False

            longer_index += 1
            shorter_index += 1

        return True


def zig_zag_string(string, height):
    height_map = {}
    for level in range(height):
        height_map[level] = []

    level, switch = 0, -1
    for char in string:
        height_map[level].append(char)

        if level == height - 1 or level == 0:
            switch *= -1

        level += switch

    result = ""
    for level in range(height):
        for char in height_map[level]:
            result += char

    return result

