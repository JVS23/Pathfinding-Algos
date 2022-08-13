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
