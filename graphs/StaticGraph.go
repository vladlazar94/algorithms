package graphs

/*
DirectedStaticGraph provides a generic implementation of a directed graph
constructed from a static list of values.
It does not support insertion of removal of nodes or edges.
*/
type DirectedStaticGraph struct {
	nodes []DirectedStaticGraphNode
}

/*
DirectedStaticGraphNode represents the underlying node structure of the DirectedStaticGraph.
It contains the node data under *value*, the indices (realtive to the node list, held by the graph)
of the out-going edges under *outEdges* and the indices of the incoming nodes under *
*/
type DirectedStaticGraphNode struct {
	value    interface{}
	outEdges []uintptr
	inEdges  []uintptr
}

/*
CreateDirectedStaticGraph initializez a DirectedStaticGraph from the given nodes and edges.
An edge is expected to be an array containing exactly two number.
The first numbers representsthe index of the node (relative to the nodes list)
from which the directed edge starts, while the second number represents the index
of the node where the edge ends.
*/
func CreateDirectedStaticGraph(values []interface{}, edges [][]uintptr) *DirectedStaticGraph {
	graphNodes := make([]DirectedStaticGraphNode, len(values))

	for i, val := range values {
		graphNodes[i].value = val
	}

	for _, edge := range edges {
		out, in := edge[0], edge[1]
		graphNodes[out].outEdges = append(graphNodes[out].outEdges, out)
		graphNodes[in].inEdges = append(graphNodes[in].inEdges, in)
	}

	return &DirectedStaticGraph{nodes: graphNodes}
}
