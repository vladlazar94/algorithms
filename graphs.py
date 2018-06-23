from collections import deque

class GraphNode: 

    def __init__ (self, data, neighbours):
        self.data = data
        self.neighbours_indices = neighbours
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
        for index in root.neighbour_indices:
            self.df_search(self.nodes[index])

    def bf_search (self, root):
        root.visited = True
        q = deque()
        q.appendleft(root)

        while len(q) > 0:
            node = q.pop()
            print(node.data)
            for index in node.neighbour_indices:
                if self.nodes[index].visited == True: continue
                self.nodes[index].visited = True
                q.appendleft(self.nodes[index])
        
    def top_sort (self):
        for node in self.nodes:
            node.incoming = 0

        for node in self.nodes:
            for index in node.neighbour_indices:
                self.nodes[index].incoming += 1
        
        top_sort = []
        queue = deque()

        for node in self.nodes:
            if node.incoming is 0:
                queue.appendleft(node)

        while len(queue) is not 0:
            node = queue.pop()
            top_sort.append(node)
            for index in node.neighbour_indices:
                neighbour = self.nodes[index]
                neighbour.incoming -= 1
                if neighbour.incoming is 0:
                    queue.appendleft(neighbour)

            
        if len(top_sort) is not len(self.nodes):
            print("Graph is not acyclical")
            return
        
        return top_sort

        
    

