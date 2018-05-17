// Problem: Write a program that replaces the emtpy spaces between words of a string with %20.

#include <iostream>
#include <string>

// O(n), where n is the number of chars in inputString.
std::string URLfy(const std::string& inputString){
    if(inputString.size() == 0){
        return "";
    }

    std::string outputString;

    bool flag = false;
    for(size_t index = 0; index < inputString.size(); index++){
        if(inputString[index] != ' '){
            outputString.push_back(inputString[index]);
            flag = true;
        }
        else if(flag){
            outputString.append("%20");
            flag = false;
        }
    }

    if(outputString.size() > 0){
        for(char i = 0; i < 3; i++){
            outputString.pop_back();
        }
    }

    return outputString;
}


