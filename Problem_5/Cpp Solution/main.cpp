// Problem_5: Write a program that checks whether two given strings are one edit away from eachother.
// Edits include inserting, removing or replacing a character.

#include <iostream>
#include <string>

// A simple print macro.
#define print(line) (std::cout << line << std::endl);

// O(n) in the size of the shorter string.
bool oneEditAway(const std::string& first, const std::string& second){
    if(std::abs((int)first.size() - (int)second.size()) > 1){
        return false;
    }

    bool oneEditAlready = false;
    if(first.size() == second.size()){
        for(int index = 0; index < first.size(); index++){
            if(first[index] != second[index]){
                if(oneEditAlready){
                    return false;
                }
                oneEditAlready = true;
            }
        }
        return true;
    }
    else{
        // Get the shorter, respectively the longer string:
        const std::string& longerString = first.size() > second.size() ? first : second;
        const std::string& shorterString = first.size() > second.size() ? second : first;

        // Loop through the string with different indices:
        size_t longerIndex = 0;
        size_t shorterIndex = 0;

        for(;shorterIndex < shorterString.size() && longerIndex < longerString.size();){

            if(shorterString[shorterIndex] != longerString[longerIndex]){
                longerIndex++;
                if(shorterString[shorterIndex] != longerString[longerIndex] or longerIndex - shorterIndex > 1){
                    return false;
                }
            }

            longerIndex++;
            shorterIndex++;
        }
        return true;
    }
}

int main() {

    // Tests:

    print(oneEditAway("abc", "abd"))  // True.
    print(oneEditAway("abc", "ab"))   // True.
    print(oneEditAway("abc", "dab"))  // False.
    print(oneEditAway("abc", "ac"))   // True.
    print(oneEditAway("abc", "aef"))  // False.
    print(oneEditAway("abd", "addd")) // False.

    return 0;
}
