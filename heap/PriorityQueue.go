package heap

/*
PriorityQueue description...
*/
type PriorityQueue struct {
	Heap []QueueNode
}

/*
QueueNode description...
*/
type QueueNode struct {
	Val      interface{}
	Priority float64
}

/*
Empty description...
*/
func (queue *PriorityQueue) Empty() bool {
	return len(queue.Heap) == 0
}

/*
Peek description...
*/
func (queue *PriorityQueue) Peek() (interface{}, float64) {
	firstNode := queue.Heap[0]
	return firstNode.Val, firstNode.Priority
}

/*
Insert description...
*/
func (queue *PriorityQueue) Insert(Val interface{}, Priority float64) {
	queue.Heap = append(queue.Heap, QueueNode{Val, Priority})
	lastNodeIndex := len(queue.Heap) - 1
	queue.siftUp(lastNodeIndex)
}

/*
Pop description...
*/
func (queue *PriorityQueue) Pop() (interface{}, float64) {
	topNode := queue.Heap[0]

	lastNodeIndex := len(queue.Heap) - 1

	queue.swap(0, lastNodeIndex)
	queue.Heap = queue.Heap[0:lastNodeIndex]

	if !queue.Empty() {
		queue.siftDown(0)
	}

	return topNode.Val, topNode.Priority
}

func (queue *PriorityQueue) swap(i, j int) {
	temp := queue.Heap[i]
	queue.Heap[i] = queue.Heap[j]
	queue.Heap[j] = temp
}

func (queue *PriorityQueue) siftDown(nodeIndex int) {
	heap := queue.Heap
	indexOfCurr := nodeIndex

	for indexOfCurr < len(heap) {
		indexOfLeft, indexOfRight := leftChildIndex(indexOfCurr), rightChildIndex(indexOfCurr)
		indexOfMax := indexOfCurr

		if indexOfLeft < len(heap) && heap[indexOfLeft].Priority > heap[indexOfMax].Priority {
			indexOfMax = indexOfLeft
		}

		if indexOfRight < len(heap) && heap[indexOfRight].Priority > heap[indexOfMax].Priority {
			indexOfMax = indexOfRight
		}

		if indexOfMax == indexOfCurr {
			return
		}

		queue.swap(indexOfMax, indexOfCurr)
		indexOfCurr = indexOfMax
	}
}

func (queue *PriorityQueue) siftUp(nodeIndex int) {
	indexOfCurr := nodeIndex

	for indexOfCurr > 0 {
		indexOfParent := parentIndex(indexOfCurr)

		if queue.Heap[indexOfParent].Priority >= queue.Heap[indexOfCurr].Priority {
			return
		}

		queue.swap(indexOfCurr, indexOfParent)
		indexOfCurr = indexOfParent
	}
}
