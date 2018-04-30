// Problem 6: Implement a method to perform a basic string compression using the count of repeated characters.
// If the resulting string is not shorter, the initial string should be returned.

#include <iostream>
#include <vector>
#include <string>

// A simple print macro.
#define print(line) (std::cout << line << std::endl);

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

    print("got Here!")

    for(size_t index = 0; index < charIndices.size() - 1; index++){
        outputString.push_back(inputString[charIndices[index]]);
        outputString.append(std::to_string((int)charIndices[index + 1] - (int)charIndices[index]));
    }

   return outputString;
}

int main(){

    print(compressString("aaabbcdddeff"))
    return 0;
}