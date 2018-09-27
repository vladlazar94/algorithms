from deque import Deque


class GraphNode:

    def __init__(self, value):
        self.value = value
        self.neighbours = set([])
        self.colour = False

    def __str__(self):
        return str(self.value)


class UndirectedGraph:

    def __init__(self, vertices, edges):
        self.nodes = {}

        for left, right in edges:

            left_vertex, right_vertex = vertices[left], vertices[right]

            if left_vertex not in self.nodes:
                self.nodes[left_vertex] = GraphNode(left_vertex)

            if right_vertex not in self.nodes:
                self.nodes[right_vertex] = GraphNode(right_vertex)

            self.nodes[left_vertex].neighbours.add(self.nodes[right_vertex])
            self.nodes[right_vertex].neighbours.add(self.nodes[left_vertex])

        for vertex in vertices:
            if vertex not in self.nodes:
                self.nodes[vertex] = GraphNode(vertex)

    def __iter__(self):
        for key in self.nodes.keys():
            yield key

    def reset(self):
        for node in self.nodes.values():
            node.colour = False

    def depth_first_search(self, vertex, func=print, reset=True):

        def recursion(node, process):
            if node.colour:
                return
            node.colour = True
            process(node.value)

            for node in node.neighbours:
                recursion(node, process)

        if reset:
            self.reset()

        root = self.nodes[vertex]
        recursion(root, func)

    def breadth_first_search(self, vertex, func=print, reset=True):
        if reset:
            self.reset()

        root = self.nodes[vertex]
        if root.colour:
            return

        root.colour = True
        queue = Deque(root)

        while not queue.empty():
            node = queue.pop_right()
            func(node.value)

            for neighbour in node.neighbours:
                if not neighbour.colour:
                    neighbour.colour = True
                    queue.push_left(neighbour)

    def breadth_first_iter(self, root, reset=True):
        """ Needs resetting after usage. """
        if reset:
            self.reset()

        root.colour = True
        queue = Deque(root)

        while not queue.empty():
            node = queue.pop_right()

            for neighbour in node.neighbours:
                if not neighbour.colour:
                    neighbour.colour = True
                    queue.push_left(neighbour)

            yield node

    def add_node(self, vertex):
        if vertex not in self.nodes:
            self.nodes[vertex] = GraphNode(vertex)

    def remove_node(self, vertex):
        if vertex in self.nodes:
            node = self.nodes[vertex]

            for neighbour in node.neighbours:
                neighbour.neighbours.remove(node)

            del node

    def connect(self, first, second):
        self.add_node(first)
        self.add_node(second)

        self.nodes[first].neighbours.add(self.nodes[second])
        self.nodes[second].neighbours.add(self.nodes[first])

    def disconnect(self, first, second):
        if first in self.nodes and second in self.nodes:
            self.nodes[first].neighbours.remove(self.nodes[second])
            self.nodes[second].neighbours.remove(self.nodes[first])

    def connected_components(self):
        self.reset()
        components = []

        for vertex in self.nodes.keys():
            if not self.nodes[vertex].colour:
                components.append(vertex)
                self.breadth_first_search(vertex, lambda x: x, False)

        self.reset()
        return components

    def is_connected(self):
        return len(self.connected_components()) == 1

    def cycles_no(self):
        edge_count, vertex_count, cycles = 0, 0, 0

        def collect(value):
            nonlocal edge_count, vertex_count
            vertex_count += 1
            node = self.nodes[value]
            edge_count += len(node.neighbours)

        for vertex in self.connected_components():
            self.breadth_first_search(vertex, collect)
            cycles += max(edge_count // 2 - vertex_count + 1, 0)
            edge_count, vertex_count = 0, 0

        return cycles

    def exists_path(self, first, second):

        def colour_blue(value):
            self.nodes[value].colour = 'blue'

        def colour_red(value):
            self.nodes[value].colour = 'red'


nodes = [0, 1, 2, 3, 4]

edges = [
    (0, 1),
    (1, 2),
    (2, 0),
    (2, 3),
    (3, 1)
]

graph = UndirectedGraph(nodes, edges)
graph.connect(8, 9)
graph.connect(9, 10)



