package graphs

/*
TopSort ...
*/
func (graph *DirectedStaticGraph) TopSort() ([]interface{}, bool) {
	graph.resetVisitedFlagForAllNodes()
	graph.resetIncomingEdgesCountForAllNodes()

	accumulatedValues := make([]interface{}, 0, len(graph.nodes))

	for i := range graph.nodes {
		graph.accumulateValues(i, &accumulatedValues)
	}

	if len(accumulatedValues) == len(graph.nodes) {
		return accumulatedValues, true
	}

	return nil, false
}

func (graph *DirectedStaticGraph) accumulateValues(startIndex int, acc *[]interface{}) {
	node := &graph.nodes[startIndex]
	if node.visited || node.incomungEdgesCount > 0 {
		return
	}

	node.visited = true
	*acc = append(*acc, node.value)

	for _, nodeIndex := range node.outEdges {
		graph.nodes[nodeIndex].incomungEdgesCount--
		graph.accumulateValues(nodeIndex, acc)
	}
}
