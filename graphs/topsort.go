package graphs

type Node struct {
	arrowsTo      []int
	arrowsInCount int
	visited       bool
}

type Graph struct {
	nodes []Node
}

func (graph *Graph) Populate(nodeCount int, arrows [][]int) {
	nodes := make([]Node, nodeCount)
	for i := range nodes {
		nodes[i] = Node{arrowsTo: []int{}, arrowsInCount: 0, visited: false}
	}

	for _, arrow := range arrows {
		from, to := arrow[0], arrow[1]
		startNode := &graph.nodes[from]
		targetNode := &graph.nodes[to]

		startNode.arrowsTo = append(startNode.arrowsTo, to)
		targetNode.arrowsInCount++
	}

	graph.nodes = nodes
}

func (graph *Graph) TopSortTraverse(startIndex int) []int {
	acc := []int{}
	node := &graph.nodes[startIndex]

	if !node.visited && node.arrowsInCount == 0 {
		acc = append(acc, startIndex)
		node.visited = true

		for _, arrowToIndex := range node.arrowsTo {
			graph.nodes[arrowToIndex].arrowsInCount--
			acc = append(acc, graph.TopSortTraverse(arrowToIndex)...)
		}
	}

	return acc
}

func (graph *Graph) TopSort() []int {
	acc := []int{}

	for i := range graph.nodes {
		acc = append(acc, graph.TopSortTraverse(i)...)
	}

	return acc
}
