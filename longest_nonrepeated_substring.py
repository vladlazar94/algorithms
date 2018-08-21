# Given a string, find the length of the longest substring without repeating characters.


def lengthOfLongestSubstring(s):

    char_map = {}

    checkpoint = -1
    longest_length = 0

    for index in range(0, len(s)):
        current_char = s[index]

        if current_char in char_map:
            if char_map[current_char] > checkpoint:

                current_length = index - checkpoint - 1
                checkpoint = char_map[current_char]

                if current_length > longest_length:
                    longest_length = current_length

        char_map[current_char] = index

    if longest_length is 0:
        return len(s)

    elif len(s) - checkpoint - 1 > longest_length:
        longest_length = len(s) - checkpoint - 1

    return longest_length







