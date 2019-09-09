package graphs

/*
DirectedStaticGraph ...
*/
type DirectedStaticGraph struct {
	nodes []directedStaticGraphNode
}

type directedStaticGraphNode struct {
	value              interface{}
	visited            bool
	outEdges           []int
	inEdges            []int
	incomungEdgesCount int
}

/*
CreateDirectedStaticGraph ...
*/
func CreateDirectedStaticGraph(values []interface{}, edges [][]int) *DirectedStaticGraph {
	graphNodes := make([]directedStaticGraphNode, len(values))

	for i, val := range values {
		graphNodes[i].value = val
	}

	for _, edge := range edges {
		out, in := edge[0], edge[1]
		graphNodes[out].outEdges = append(graphNodes[out].outEdges, out)
		graphNodes[in].inEdges = append(graphNodes[in].inEdges, in)
	}

	graph := DirectedStaticGraph{nodes: graphNodes}
	graph.resetIncomingEdgesCountForAllNodes()

	return &graph
}

func (graph *DirectedStaticGraph) resetIncomingEdgesCountForAllNodes() {
	for i := range graph.nodes {
		graph.nodes[i].incomungEdgesCount = len(graph.nodes[i].inEdges)
	}
}

func (graph *DirectedStaticGraph) resetVisitedFlagForAllNodes() {
	for i := range graph.nodes {
		graph.nodes[i].visited = false
	}
}
