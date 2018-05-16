// Problem_5: Write a program that checks whether two given strings are one edit away from eachother.
// Edits include inserting, removing or replacing a character.

package main

import "math"

// O(n) in the size of the shorter string.
func isOneEditAway(firstString string, secondString string) bool {

	if math.Abs(float64(len(firstString))-float64(len(secondString))) > 1 {
		return false
	}

	if len(firstString) == len(secondString) {
		oneEditAlready := false
		for index := 0; index < len(firstString); index++ {
			if firstString[index] != secondString[index] {
				if oneEditAlready {
					return false
				}
				oneEditAlready = true
			}
		}
		return true
	} else {

		// Store the longer and shorter strings via points, to avoid copying them.
		var longerStringPtr *string
		var shorterStringPtr *string

		if len(firstString) > len(secondString) {
			longerStringPtr = &firstString
			shorterStringPtr = &secondString
		} else {
			longerStringPtr = &secondString
			shorterStringPtr = &firstString
		}

		longerIndex := 0
		shorterIndex := 0

		for shorterIndex < len(*shorterStringPtr) && longerIndex < len(*longerStringPtr) {
			if (*shorterStringPtr)[shorterIndex] != (*longerStringPtr)[longerIndex] {
				longerIndex++
				if (*shorterStringPtr)[shorterIndex] != (*longerStringPtr)[longerIndex] || longerIndex-shorterIndex > 1 {
					return false
				}
			}
			shorterIndex++
			longerIndex++
		}
		return true
	}

}

func main() {

	println(isOneEditAway("abc", "abd"))  // True.
	println(isOneEditAway("abc", "ab"))   // True.
	println(isOneEditAway("abc", "dab"))  // False.
	println(isOneEditAway("abd", "addd")) // False.

}
