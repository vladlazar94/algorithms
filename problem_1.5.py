# Problem_5: Write a program that checks whether 
# two given strings are one edit away from eachother.
# Edits include inserting, removing or replacing a character.

def one_edit_away (first, second):
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

