package graphs

/*
DirectedStaticGraph provides a generic implementation of a directed graph
constructed from a static list of values.
It does not support insertion of removal of nodes or edges.
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
CreateDirectedStaticGraph initializez a DirectedStaticGraph from the given nodes and edges.
An edge is expected to be an array containing exactly two number.
The first numbers representsthe index of the node (relative to the nodes list)
from which the directed edge starts, while the second number represents the index
of the node where the edge ends.
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
