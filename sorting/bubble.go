package sorting

func bubble(nums []float64) {
	for i := 1; i < len(nums); i++ {
		if nums[i] < nums[i-1] {
			aux := nums[i-1]
			nums[i-1] = nums[i]
			nums[i] = aux
		}
	}

	if len(nums) > 2 {
		bubble(nums[0 : len(nums)-1])
	}
}
