// Problem 6: Implement a method to perform a basic string compression using the count of repeated characters.
// If the resulting string is not shorter, the initial string should be returned.

#include <iostream>
#include <vector>
#include <string>

// A simple print macro.
#define print(line) (std::cout << line << std::endl);

// O(n) in the length of the input string. Note: This implementation makes use of an additional vector to store idices.
// This can be avoided by constructing the output string directly (with a slightly bushier code).
std::string compressString(const std::string& inputString){

    if(inputString.size() < 2){
        return inputString;
    }

    std::string outputString;
    std::vector<size_t> charIndices;
    charIndices.push_back(0);

    for(size_t index = 1; index < inputString.size(); index++){

        if(inputString[index] != inputString[index - 1]){
            charIndices.push_back(index);
        }
    }
    charIndices.push_back(inputString.size());

    unsigned int count = 0;
    for(size_t index = 0; index < charIndices.size() - 1; index++){

        count = (unsigned int)charIndices[index + 1] - (unsigned int)charIndices[index];

        outputString.push_back(inputString[charIndices[index]]);
        if(count > 1){
            outputString.append(std::to_string(count));
        }
    }

    if(outputString.size() >= inputString.size()){
        return inputString;
    }
    return outputString;
}

int main(){

    print(compressString("aaabbcdddeff"))
    print(compressString("abc"))
    return 0;
}