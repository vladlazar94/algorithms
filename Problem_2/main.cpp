// Problem_2: Write a program that checks whether two strings are perumations of eachother.

#include <iostream>
#include <array>
#include <string>

bool stringsArePermutations(const std::string& firstString, const std::string& secondString){

    if(firstString.size() != secondString.size()){
        return false;
    }

    // Assuming that the strings consists of ASCII chars.
    std::array<bool, 255> charHashArray{false};

    for(int i = 0; i < firstString.size(); i++){
        charHashArray[(size_t)firstString[i]] = true;
    }

    for(int i = 0; i < secondString.size(); i++){
        if(charHashArray[(size_t)secondString[i]] == false){
            return false;
        }
    }

    return true;
}

int main(){

    std::cout<<stringsArePermutations("abc", "bac")<<std::endl;
    std::cout<<stringsArePermutations("abc", "bcd")<<std::endl;

    return 0;
}
