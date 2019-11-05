package sorting

import "math"

func merge(nums []float64) {
	if len(nums) <= 1 {
		return
	}

	mid := len(nums) / 2

	merge(nums[0:mid])
	merge(nums[mid:len(nums)])

	combine(nums[0:mid], nums[mid:len(nums)], nums)
}

func combine(left, right, container []float64) {
	leftCopy := make([]float64, len(left)+1)
	rightCopy := make([]float64, len(right)+1)

	for i := range left {
		leftCopy[i] = left[i]
	}

	for i := range right {
		rightCopy[i] = right[i]
	}

	leftCopy[len(left)] = math.Inf(1)
	rightCopy[len(right)] = math.Inf(1)

	l, r := 0, 0
	for i := range container {
		if leftCopy[l] < rightCopy[r] {
			container[i] = leftCopy[l]
			l++
		} else {
			container[i] = rightCopy[r]
			r++
		}
	}
}
