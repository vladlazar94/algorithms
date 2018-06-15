# Problem 6: Implement a method to perform a basic string compression using the count of repeated 
# characters. If the resulting string is not shorter, the initial string should be returned.

def compress (string):
    if len(string) < 2:
        return string

    indices = [0]
    for index in range (1, len(string)):
        if string[index] is not string[index - 1]:
            indices.append(index)
    indices.append(len(string))

    count = 0
    output = ""
    for index in range(0, len(indices) - 1):

        output += string[indices[index]]
        count = indices[index + 1] - indices[index]
        if count > 1:
            output += str(count) 

    if len(output) > len(string):
        return string
    return output
