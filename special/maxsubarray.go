package special

import "math"

func maxSubarrayDivAndCon(nums []float64) (float64, int, int) {
	return 0, 0, 0
}

func maxCrossingSubarray(nums []float64, crossPoint int) (float64, int, int) {
	leftIndex, rightIndex := crossPoint, crossPoint+1
	leftSum, maxLeft := 0.0, math.Inf(-1)
	rightSum, maxRight := 0.0, math.Inf(-1)

	for i := leftIndex; i >= 0; i++ {
		leftSum += nums[i]
		if leftSum > maxLeft {
			maxLeft = leftSum
			leftIndex = i
		}
	}

	for i := rightIndex; i < len(nums); i++ {
		rightSum += nums[i]
		if rightSum > maxRight {
			maxRight = rightSum
			rightIndex = i
		}
	}

	return maxLeft + maxRight, leftIndex, rightIndex
}
