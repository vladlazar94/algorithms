// Problem 6: Implement a method to perform a basic string compression using the count of repeated characters.
// If the resulting string is not shorter, the initial string should be returned.

package main

import "strconv"

func compressString(inputString string) string {

	if len(inputString) < 3 {
		return inputString
	}

	var outputString string
	count := 1

	for index := 1; index < len(inputString); index++ {

		if inputString[index] != inputString[index-1] {
			if count > 1 {
				outputString = outputString + string(inputString[index-1]) + strconv.Itoa(count)
			} else {
				outputString = outputString + string(inputString[index-1])
			}
			count = 1
		} else {
			count++
		}
	}
	if count > 1 {
		outputString = outputString + string(inputString[len(inputString)-1]) + strconv.Itoa(count)
	} else {
		outputString = outputString + string(inputString[len(inputString)-1])
	}

	if len(outputString) > len(inputString) {
		return inputString
	}
	return outputString
}

func main() {

	println(compressString("abbbc"))

}
