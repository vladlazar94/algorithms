package sorting

func search(nums []float64, num float64) int {
	if len(nums) == 0 {
		return -1
	}

	mid := len(nums) / 2

	switch true {
	case num == nums[mid]:
		return mid

	case num < nums[mid]:
		i := search(nums[0:mid], num)
		if i != -1 {
			return i
		}

	case num > nums[mid]:
		i := search(nums[mid+1:len(nums)], num)
		if i != -1 {
			return mid + i + 1
		}
	}

	return -1
}
