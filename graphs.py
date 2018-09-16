from deque import Deque


class GraphNode:

    def __init__(self, value):
        self.value = value
        self.neighbours = set([])
        self.visited = False

    def __str__(self):
        return str(self.value)


class UndirectedGraph:
    def __init__(self, vertices, edges):
        self.nodes = list(set([GraphNode(vertex) for vertex in vertices]))

        self.registry = dict([(vertex, node) for vertex, node
                              in zip(vertices, self.nodes)])

        for source, target in edges:
            self.nodes[source].neighbours.add(target)
            self.nodes[target].neighbours.add(source)

    def reset_visited(self):
        for node in self.nodes:
            node.visited = False

    def df_search(self, root, func=print):
        if root.visited:
            return
        root.visited = True
        func(root.value)

        for index in root.neighbours:
            self.df_search(self.nodes[index])

    def bf_search(self, vertex, func=print):
        root = self.registry[vertex]
        root.visited = True
        queue = Deque(root)

        while not queue.empty():
            node = queue.pop_right()
            func(node.value)

            for index in node.neighbours:
                neighbour = self.nodes[index]
                if not neighbour.visited:
                    queue.push_left(neighbour)
                neighbour.visited = True

    def insert(self, vertex):
        if vertex not in self.registry:
            self.nodes.append(GraphNode(vertex))
            self.registry[vertex] = self.nodes[-1]


nodes = [0, 1, 2, 3, 4]

edges = [
    (0, 1),
    (1, 2),
    (2, 0),
    (2, 3),
    (3, 1)
]

graph = UndirectedGraph(nodes, edges)


