package dynamicprogramming

/*
Given a string, your task is to count how many palindromic substrings are there in the string.
The substrings with different start or end indices are counted as different substrings even if
they consist of the same characters.
*/
func countSubstrings(s string) int {
	total := 0
	startIndices := []int{}

	for i := range s {
		total++
		startIndices = append(startIndices, i)
		updated := []int{i}

		for _, index := range startIndices {
			oneToLeft := index - 1
			if oneToLeft >= 0 && s[i] == s[oneToLeft] {
				total++
				updated = append(updated, oneToLeft)
			}
		}

		startIndices = updated
	}

	return total
}
