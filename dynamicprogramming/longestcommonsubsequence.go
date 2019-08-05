package dynamicprogramming

/*
Given two strings text1 and text2, return the length of their longest common subsequence.
A subsequence of a string is a new string generated from the original string with some
characters(can be none) deleted without changing the relative order of the remaining characters.
(eg, "ace" is a subsequence of "abcde" while "aec" is not).
A common subsequence of two strings is a subsequence that is common to both strings.
If there is no common subsequence, return 0.
*/
func longestCommonSubsequence(first string, second string) int {
	partials := make([][]int, len(first)+1)
	for i := range partials {
		partials[i] = make([]int, len(second)+1)
	}

	for i, charFirst := range first {
		for j, charSecond := range second {
			if charFirst == charSecond {
				partials[i+1][j+1] = 1 + partials[i][j]
			} else {
				partials[i+1][j+1] = max(partials[i][j+1], partials[i+1][j])
			}
		}
	}

	return partials[len(first)][len(second)]
}
