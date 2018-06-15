# Problem 1.3: Write a program that replaces the 
# emtpy spaces between words of a string with %20.

def URLfy (string):  
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

    output = output[0 : len(output) - 2]
    return output

print(URLfy("aa bb cc"))