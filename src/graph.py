import random
import networkx as nx
import netxfuncs as nxf


class Graph:
    """Class for generating and modifying graphs.
    """

    def __init__(self, len_v):
        """Initializes the graph with an adjacency list filled with -1's representing the lack of
        an edge between two vertices.

        Args:
            len_v: The amount of vertices assigned to the created graph.
        """

        self.vertices = len_v
        self.edge = [[-1 for i in range(len_v)] for j in range(len_v)]
        self.seen = []
        self.nx_graph = nx.Graph()

    def add(self, start, end, weight):
        """A method for adding edges between vertices. The vertices are numbered by the indexes at this stage.
        The start/end order doesn't matter since it's an undirected graph.

        Args:
            start: The first vertix to update.
            end: The second vertix to update.
            weight: Weight for the edge, set to 1 for simulating an unweighted graph.
        """
        self.edge[start][end] = weight
        self.edge[end][start] = weight

        self.nx_graph.add_edge(start, end, weight=weight)

    def generate(self, size):
        """A method for generating a random graph of given size with edges weighting 1-10 units.
        Works the best with sizes between 5-20.
        """

        for i in range(size):
            if i == size - 1:
                return
            chance = random.randint(0, 10)
            weight = random.randint(1, 10)

            self.add(i, i+1, weight)

            if chance >= 6:
                shortcut_node = random.randint(0, size - 1)
                while shortcut_node == i:
                    shortcut_node = random.randint(0, size - 1)
                self.add(i, shortcut_node,
                         random.randint(1, 10))
