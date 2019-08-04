package dynamicprogramming

/*
Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.
You have the following 3 operations permitted on a word:
Insert a character
Delete a character
Replace a character
*/
func editDistance(first string, second string) int {
	partials := make([][]int, len(first)+1)
	for p := range partials {
		partials[p] = make([]int, len(second)+1)
	}

	for i := range first {
		partials[i+1][0] = i + 1
	}

	for j := range second {
		partials[0][j+1] = j + 1
	}

	for i, charFirst := range first {
		for j, charSecond := range second {

			if charFirst == charSecond {
				partials[i+1][j+1] = partials[i][j]
			} else {
				partials[i+1][j+1] = 1 + min(
					partials[i][j],
					partials[i+1][j],
					partials[i][j+1],
				)
			}
		}
	}

	return partials[len(first)][len(second)]
}
