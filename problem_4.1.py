# Problem 4.1: Given a directed graph, design an algorithm to find out
# whether there exists a route between two given nodes.

from collections import deque

class GraphNode: 
    def __init__ (self, data, neighbours):
        self.data = data
        self.neighbours = neighbours
        self.visited = False

class Graph:
    def __init__ (self):
        self.nodes = []

    def reset (self):
        for node in self.nodes:
            node.visited = False

    def push (self, node): 
        self.nodes.append(node)

def exists_route (graph, firstNode, secondNode):
    if not firstNode in graph.nodes or not secondNode in graph.nodes: return False
    if firstNode == secondNode: return True

    firstNode = graph.nodes[graph.nodes.index(firstNode)]
    secondNode = graph.nodes[graph.nodes.index(secondNode)]
    
    q = deque()
    firstNode.visited = 'red'
    q.appendleft(firstNode)
    
    while len(q) > 0:  
        node = q.pop()
        if node == secondNode: return True 
        for index in node.neighbours:
            if not graph.nodes[index].visited == 'red': 
                graph.nodes[index].visited = 'red'
                q.appendleft(graph.nodes[index])
    
    return False
            
        






nodes = []
graph = Graph()
nodes.append(GraphNode('A', [1]))
nodes.append(GraphNode('B', [2, 3]))
nodes.append(GraphNode('C', [3]))
nodes.append(GraphNode('D', [4, 1]))
nodes.append(GraphNode('E', [5, 0, 1]))
nodes.append(GraphNode('F', [0]))
nodes.append(GraphNode('G', []))
for node in nodes:
    graph.push(node)

print(exists_route(graph, graph.nodes[3], graph.nodes[6]))


