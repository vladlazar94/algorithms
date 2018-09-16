from deque import Deque


class GraphNode:

    def __init__(self, value, neighbours=None):
        self.value = value
        self.neighbours = [] if not neighbours else neighbours
        self.incoming = []
        self.visited = False


class Graph:

    def __init__(self, nodes):
        self.nodes = nodes
        for node_index in range(len(nodes)):
            curr_node = self.nodes[node_index]
            for neighbour_index in curr_node.neighbours:
                self.nodes[neighbour_index].incoming.append(node_index)

    def reset(self):
        for node in self.nodes:
            node.visited = False

    def df_search(self, root, func):
        if root.visited:
            return
        root.visited = True

        func(root.value)

        for neighbour in root.neighbours:
            self.df_search(self.nodes[neighbour], func)

    def bf_search(self, root, func=print):
        root.visited = True
        deque = Deque(root)

        while not deque.empty():
            node = deque.pop_right()
            func(node.value)

            for index in node.neighbours:
                neighbour = self.nodes[index]
                if not neighbour.visited:
                    deque.push_left(neighbour)
                neighbour.visited = True

    def is_connected(self):
        self.reset()
        self.bf_search(self.nodes[0])

        for node in self.nodes:
            if not node.visited:
                self.reset()
                return False

        self.reset()
        return True





n0 = GraphNode(0, [2, 3])
n1 = GraphNode(1, [0, 5])
n2 = GraphNode(2, [1, 5])
n3 = GraphNode(3, [5, 4])
n4 = GraphNode(4, [])
n5 = GraphNode(5, [0, 1, 2, 3])
gr = Graph([n0, n1, n2, n3, n4, n5])

gr.bf_search(n1)
