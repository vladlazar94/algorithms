package dynamicprogramming

/*
You are a professional robber planning to rob houses along a street.
Each house has a certain amount of money stashed,
the only constraint stopping you from robbing each of them is that
adjacent houses have security system connected and it will automatically
contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house,
determine the maximum amount of money you can rob tonight without alerting the police.
*/
func robHouse(nums []int) int {
	if len(nums) == 0 {
		return 0
	}
	max, _ := robHouseSubProblem(nums)
	return max
}

func robHouseSubProblem(nums []int) (int, int) {
	if len(nums) == 1 {
		return nums[0], 0
	}

	current := nums[0]
	subMax, withoutFirst := robHouseSubProblem(nums[1:])

	return max(subMax, current+withoutFirst), subMax
}
