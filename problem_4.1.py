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
    def one_way(graph, firstNode, secondNode):
        
        if not firstNode in graph.nodes or not secondNode in graph.nodes: return False
        if firstNode == secondNode: return True
        graph.reset()

        firstNode = graph.nodes[graph.nodes.index(firstNode)]
        secondNode = graph.nodes[graph.nodes.index(secondNode)]
    
        q = deque()
        firstNode.visited = True
        q.appendleft(firstNode)
    
        while len(q) > 0:  
            node = q.pop()
            if node == secondNode: return True 
            for index in node.neighbours:
                if not graph.nodes[index].visited == True: 
                    graph.nodes[index].visited = True
                    q.appendleft(graph.nodes[index])
    
        return False
    
    return one_way(graph, firstNode, secondNode) or one_way(graph, secondNode, firstNode)


