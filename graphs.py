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

    def df_search (self, root):
        if root.visited == True: return
        root.visited = True
        print(root.data)
        for index in root.neighbours:
            self.df_search(self.nodes[index])

    def bf_search (self, root):
        root.visited = True
        q = deque()
        q.appendleft(root)

        while len(q) > 0:
            node = q.pop()
            print(node.data)
            for index in node.neighbours:
                if self.nodes[index].visited == True: continue
                self.nodes[index].visited = True
                q.appendleft(self.nodes[index])
        


