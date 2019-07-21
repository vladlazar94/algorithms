package dynamicprogramming

/*
Given an integer array nums, find the contiguous subarray (containing at least one number)
which has the largest sum and return its sum.
*/
func maxSubArray(nums []int) int {
	res, _ := maxSubArraySubProblem(nums)
	return res
}

func maxSubArraySubProblem(nums []int) (int, int) {
	if len(nums) == 1 {
		return nums[0], max(0, nums[0])
	}

	firstNumber := nums[0]
	subMax, bestExtension := maxSubArraySubProblem(nums[1:])
	extended := firstNumber + bestExtension

	return max(subMax, extended), max(0, extended)
}
