package special

import "math"

/*
CoinCombinations returns the number of linear combinations of coin values amounting to the target sum.
Notations:
    Coins               -> the collection of coin values
    Coins[i]            -> the ith coin value
    Solution(target, n) -> the number linear combinations of the first n coin values amounting to the target

Recursion:
    Solution(target, n) = Solution(target, n-1) + Solution(target - Coins[n], n)

Complexity:
    O(target * n) time | Theta(target) space, where n is the number of coin values
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

/*
MinCoinCombinations returns the minimum number of coins required to amount up to the target value.
Notations:
	Coins 			 -> the coin values
	Coins[i] 		 -> the ith coin value
	Solution(target) -> the minimum number of coins that added up amount to target

Insights:
	For any non-zero target, the a solution representing the smallest set of coins that add up to
	the target must contain at least one coin. The rest of the coins comprised in the solution
	must necessarily yield a solution to the same problem with a new target equal to the target
	minus the value of that one coin. This allows us to relate the problem determined by the target
	and the set of coins to a problem determined by a lower target and the same set of coins,
	as is captured in the following recursion.

Recursion:
	Solution(target) = Max({1 + Solution(target - Coins[i]) | i from 0 to number of coin values})

Complexity:
	O(target * n) time | Theta(target) space, where n is the number of coin values
*/
func MinCoinCombinations(target int, coinValues []int) int {
	partialSolutions := make([]int, target+1)

	for i := 1; i < len(partialSolutions); i++ {
		partialSolutions[i] = math.MaxInt32
	}

	for i := range partialSolutions {
		for _, value := range coinValues {
			if value <= i {
				partialSolutions[i] = Min(partialSolutions[i], partialSolutions[i-value]+1)
			}
		}
	}

	if partialSolutions[target] == math.MaxInt32 {
		return -1
	}

	return partialSolutions[target]
}
