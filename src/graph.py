import random
import networkx as nx
import netxfuncs as nxf
import math


class Graph:
    """Class for generating and modifying graphs.
    """

    def __init__(self, len_v):
        """Initializes the graph with an adjacency list filled with -1's representing the lack of
        an edge between two vertices.

        Args:
            len_v: The amount of vertices assigned to the created graph.
        """

        self.vertices_amount = len_v
        self.nodes = []
        self.edge = [[-1 for i in range(len_v)] for j in range(len_v)]
        self.seen = []
        self.nx_graph = nx.Graph()

    def add_edgex(self, start, end):
        """A method for adding edges between vertices. The vertices are numbered by the indexes at this stage.
        The start/end order doesn't matter since it's an undirected graph.

        Args:
            start: The first vertix to update.
            end: The second vertix to update.
            weight: Weight for the edge, set to 1 for simulating an unweighted graph.
        """

        weight = math.sqrt(((self.nodes[end][0]-self.nodes[start][0])
                           ** 2 + (self.nodes[end][1] - self.nodes[start][1])**2))

        rounded_weight = round(weight, 2)
        self.edge[start][end] = rounded_weight
        self.edge[end][start] = rounded_weight

        self.nx_graph.add_edge(start, end, weight=rounded_weight)

    def generate_nodes(self, size):
        """A method for generating a random graph of given size with edges weighting 1-10 units.
        Works the best with sizes between 5-20.
        """

        for i in range(size):
            if i == size:
                return

            xpos = random.randint(1, 100)
            ypos = random.randint(1, 100)

            self.nodes.append([xpos, ypos])

            self.nx_graph.add_node(i, pos=(xpos, ypos))

    def generate_edges(self, size):
        """A method for generating a random graph of given size with edges weighting 1-10 units.
        Works the best with sizes between 5-20.
        """

        for i in range(size):
            if i == size - 1:
                return
            chance = random.randint(0, 10)
            xpos = random.randint(1, 100)
            ypos = random.randint(1, 100)

            self.add_edgex(i, i+1)
            self.nx_graph.add_edge(i, i+1)

            if chance >= 6:
                shortcut_node = random.randint(0, size - 1)
                while shortcut_node == i:
                    shortcut_node = random.randint(0, size - 1)
                self.add_edgex(i, shortcut_node)
                self.nx_graph.add_edge(i, shortcut_node)
