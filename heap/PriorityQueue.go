package heap

/*
PriorityQueue description...
*/
type PriorityQueue struct {
	heap []int
}

/*
Empty description...
*/
func (queue *PriorityQueue) Empty() bool {
	return len(queue.heap) == 0
}

/*
Push description...
*/
func (queue *PriorityQueue) Push(num int) {
	queue.heap = append(queue.heap, num)
	queue.siftUp(len(queue.heap) - 1)
}

/*
ExtractMax description...
*/
func (queue *PriorityQueue) ExtractMax() int {
	max := queue.heap[0]
	lastElemIndex := queue.heap[len(queue.heap)-1]

	queue.swap(0, lastElemIndex)
	queue.heap = queue.heap[0:lastElemIndex]
	queue.siftDown(0)

	return max
}

/*
Peek description
*/
func (queue *PriorityQueue) Peek() int {
	return queue.heap[0]
}

func (queue *PriorityQueue) swap(i, j int) {
	heap := queue.heap
	temp := heap[i]
	heap[i] = heap[j]
	heap[j] = temp
}

func (queue *PriorityQueue) siftDown(i int) {
	current := i
	heap := queue.heap

	for current < len(heap) {
		left, right := leftChildIndex(current), rightChildIndex(current)
		max := current

		if left < len(heap) && heap[left] > heap[max] {
			max = left
		}

		if right < len(heap) && heap[right] > heap[max] {
			max = right
		}

		if max == current {
			return
		}

		queue.swap(current, max)
		current = max
	}
}

func (queue *PriorityQueue) siftUp(i int) {
	heap := queue.heap
	current := i

	for current > 0 {
		parentIndex := parentIndex(i)

		if heap[parentIndex] >= heap[current] {
			return
		}

		queue.swap(current, parentIndex)
		current = parentIndex
	}
}
