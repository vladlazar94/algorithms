package heap

/*
MaxBinaryHeap description...
*/
type MaxBinaryHeap struct {
	nums []int
}

/*
Insert description...
*/
func (heap *MaxBinaryHeap) Insert(num int) {

}

/*
Pop description...
*/
func (heap *MaxBinaryHeap) Pop() int {
	return 0
}

/*
Peek description...
*/
func (heap *MaxBinaryHeap) Peek() int {
	return 0
}

func (heap *MaxBinaryHeap) leftChild(i int) int {
	return 2*i + 1
}

func (heap *MaxBinaryHeap) rightChild(i int) int {
	return 2*i + 2
}

func (heap *MaxBinaryHeap) parent(i int) int {
	return (i - 1) / 2
}

func (heap *MaxBinaryHeap) siftDown() {

}
