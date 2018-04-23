// Problem_1: Write a program that detects whether a string has all unique characters.

#include <string>
#include <array>
#include <iostream>

// Time: O(n) Space: o
bool uniqueCharacters(const std::string& inputString){
    // Assuming the string consists of ASCII characters,
    // of which there are at most 255.
    std::array<bool, 255> charArray{false};

    // Don't loop further than needed.
    size_t indexLimit = 128;
    if(inputString.size() < indexLimit){
        indexLimit = inputString.size();
    }

    // Most basic of hashing functions. Who doesn't like
    // the identity transform?
    for(int i = 0; i < indexLimit; i++){
        if(charArray[(size_t)inputString[i]]){
            return false;
        }
        charArray[(size_t)inputString[i]] = true;
    }
    return true;
}


int main(){
    // Now to test this arcane code.
    std::string str1 = "aherqmca";
    std::string str2 = "asdfghjkl";

    std::cout<<uniqueCharacters(str1)<<std::endl; // True.
    std::cout<<uniqueCharacters(str2)<<std::endl; // False.

    return 0;
}
