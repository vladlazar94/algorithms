package special

/*
MaxSubarraySum returns the highest sum over all contiguous subarrays of the input array.
Notations:
	Solution(n) -> the solution for the first n elements of the array

Sketch:
	{ * * * * * * * * * * * * * * * * * (*) * * * * * * }
                                         i -> current index

	[           Dolution(i-1)            ]
	   [ Best sum ]
						[  Best sum @end ]

Complexity:
	Theta(n) time | Theta(1) space, where n is the number of numbers in the input array.
*/
func MaxSubarraySum(nums []int) int {
	bestSum := 0
	bestSumAdjacentToEnd := 0

	for _, num := range nums {
		bestSumAdjacentToEnd = Max(0, num+bestSumAdjacentToEnd)
		bestSum = Max(bestSum, bestSumAdjacentToEnd)
	}

	return bestSum
}
