package dynamicprogramming

// MaxSubArray finds the sum of the contiguous subarray with the largest sum.
func MaxSubArray(nums []int) int {
	res, _ := solveSubProblem(nums)
	return res
}

func solveSubProblem(nums []int) (int, int) {
	if len(nums) == 1 {
		return nums[0], max(0, nums[0])
	}

	firstNumber := nums[0]
	subMax, bestExtension := solveSubProblem(nums[1:])
	extended := firstNumber + bestExtension

	return max(subMax, extended), max(0, extended)
}
