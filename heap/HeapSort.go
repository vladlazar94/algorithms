package heap

/*
HeapSort description...
*/
func HeapSort(nums []int) {
	if len(nums) < 2 {
		return
	}

	buildHeap(nums, len(nums))

	for i := len(nums) - 1; i > 0; i-- {
		swap(nums, i, 0)
		siftDown(nums, 0, i)
	}
}

func buildHeap(nums []int, heapEnd int) {
	lastParentIndex := parent(nums, heapEnd-1)

	for i := lastParentIndex; i >= 0; i-- {
		siftDown(nums, i, heapEnd)
	}
}

func siftDown(nums []int, nodeIndex int, heapEnd int) {
	currentIndex := nodeIndex

	for currentIndex < heapEnd {
		leftIndex, rightIndex := leftChild(nums, currentIndex), rightChild(nums, currentIndex)

		max := currentIndex

		if leftIndex < heapEnd && nums[leftIndex] > nums[max] {
			max = leftIndex
		}

		if rightIndex < heapEnd && nums[rightIndex] > nums[max] {
			max = rightIndex
		}

		if currentIndex == max {
			return
		}

		swap(nums, currentIndex, max)
		currentIndex = max
	}

}

func swap(nums []int, i int, j int) {
	temp := nums[i]
	nums[i] = nums[j]
	nums[j] = temp
}

func leftChild(nums []int, i int) int {
	return 2*i + 1
}

func rightChild(nums []int, i int) int {
	return 2*i + 2
}

func parent(nums []int, i int) int {
	return (i - 1) / 2
}
