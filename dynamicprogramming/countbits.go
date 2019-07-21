package dynamicprogramming

/*
Given a non negative integer number num.
For every numbers i in the range 0 ≤ i ≤ num calculate the number
of 1's in their binary representation and return them as an array.
*/
func countBits(num int) []int {
	highestPower := 1
	counts := make([]int, num+1)

	for i := range counts[1:] {
		currentNum := i + 1
		if currentNum >= 2*highestPower {
			highestPower *= 2
		}
		counts[currentNum] = 1 + counts[currentNum-highestPower]
	}

	return counts
}
