// Problem_2: Write a program that checks whether two strings are perumations of eachother.

#include <iostream>
#include <array>
#include <string>

// O(n+m) in the number of elements in each string.
bool stringsArePermutations(const std::string& firstString, const std::string& secondString){

    if(firstString.size() != secondString.size()){
        return false;
    }

    // Assuming that the strings consists of ASCII chars.
    std::array<int, 255> charHashArray{0};

    for(size_t i = 0; i < firstString.size(); i++){
        charHashArray[(size_t)firstString[i]]++;
    }

    for(size_t i = 0; i < secondString.size(); i++){
        charHashArray[(size_t)secondString[i]]--;
        if(charHashArray[(size_t)secondString[i]] < 0){
            return false;
        }
    }

    return true;
}


