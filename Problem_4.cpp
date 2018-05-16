// Problem_4: Write a program that checks whether a given string is a permutation of a palindrome.

#include <iostream>
#include <string>
#include <array>

// O(n) in the number of chars in inputString.
bool palindromePermutation(const std::string& inputString){
    // Assuming that the input string consists of ASCII chars.
    std::array<bool, 255> charHashArray{false};

    int palindromeCount = 0;
    int hashIndex = 0;

    for(size_t index = 0; index < inputString.size(); index++){
        hashIndex = (int)inputString[index];
        if(charHashArray[hashIndex] == true){
            palindromeCount--;
            charHashArray[hashIndex] == false;
        }
        else{
            palindromeCount++;
            charHashArray[hashIndex] = true;
        }
    }

    if(palindromeCount == 0 or palindromeCount == 1){
        return true;
    }
    return false;
}

int main(){

    std::cout<<palindromePermutation("aabcdbc")<<std::endl; // True.
    std::cout<<palindromePermutation("abcdaef")<<std::endl; // False.

    return 0;
}
