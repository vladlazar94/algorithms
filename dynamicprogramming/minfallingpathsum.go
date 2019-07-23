package dynamicprogramming

/*
Given a square array of integers A, we want the minimum sum of a falling path through A.
A falling path starts at any element in the first row, and chooses one element from each row.
The next row's choice must be in a column that is different from the previous row's column by at most one.
*/
func minFallingPathSum(A [][]int) int {
	return min(minSumForEachTopElement(A)...)
}

func minSumForEachTopElement(A [][]int) []int {
	if len(A) == 1 {
		return A[0]
	}

	currentRow := A[0]
	minSumsBelow := minSumForEachTopElement(A[1:])
	minSums := make([]int, len(currentRow))

	for i := 1; i < len(currentRow)-1; i++ {
		minSums[i] = currentRow[i] +
			min(
				minSumsBelow[i-1],
				minSumsBelow[i],
				minSumsBelow[i+1],
			)
	}

	li := len(currentRow) - 1
	minSums[0] = currentRow[0] + min(minSumsBelow[0], minSumsBelow[1])
	minSums[li] = currentRow[li] + min(minSumsBelow[li-1], minSumsBelow[li])

	return minSums
}
