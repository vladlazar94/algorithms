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
        self.nodes = [GraphNode(vertex) for vertex in vertices]

        self.registry = dict([(vertex, node)
                              for vertex, node in zip(vertices, self.nodes)])

        for left, right in edges:
            self.nodes[left].neighbours.add(self.nodes[right])
            self.nodes[right].neighbours.add(self.nodes[left])

    def reset(self):
        for node in self.nodes:
            node.visited = False

    def df_search(self, vertex, func=print, reset=True):

        def recursion(node, func):
            if node.visited:
                return
            node.visited = True
            func(node)

            for neighbour in node.neighbours:
                recursion(neighbour, func)

        if reset:
            self.reset()

        root = self.registry[vertex]
        recursion(root, func)

    def bf_search(self, vertex, func=print, reset=True):
        if reset:
            self.reset()

        root = self.registry[vertex]
        root.visited = True
        queue = Deque(root)

        while not queue.empty():
            node = queue.pop_right()
            func(node.value)

            for neighbour in node.neighbours:
                if not neighbour.visited:
                    neighbour.visited = True
                    queue.push_left(neighbour)

    def add_node(self, vertex):
        if vertex not in self.registry:
            self.registry[vertex] = GraphNode(vertex)
            self.nodes.append(self.registry[vertex])

    def connect(self, first, second):
        self.add_node(first)
        self.add_node(second)

        self.registry[first].neighbours.add(self.registry[second])
        self.registry[second].neighbours.add(self.registry[first])


nodes = [0, 1, 2, 3, 4]

edges = [
    (0, 1),
    (1, 2),
    (2, 0),
    (2, 3),
    (3, 1)
]

graph = UndirectedGraph(nodes, edges)

graph.bf_search(0)


