package dynamicprogramming

/*
CoinCombinations returns the number of linear combinations of coin values amounting to the target sum.
Notations:
    Coins               -> the collection of coin values
    Coins[i]            -> the ith coin value
    Solution(target, n) -> the number linear combinations of the first n coin values amounting to the target

Recursion:
    Solution(target, n) = Solution(target, n-1) + Solution(target - Coins[n], n)

Complexity:
    Theta(target * n) time | Theta(target) space, where n is the number of coin values
*/
func CoinCombinations(target int, coinValues []int) int {
	partialSolutions := append([]int{1}, make([]int, target)...)

	for _, value := range coinValues {
		for i := range partialSolutions {
			if i-value >= 0 {
				partialSolutions[i] += partialSolutions[i-value]
			}
		}
	}

	return partialSolutions[target]
}
