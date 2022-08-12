from queue import PriorityQueue


class Algos():
    """The algorithms in this class are used for testing the raw algorithms, instead of
    the ones in main, because the accuracy of the statistics made with
    those would be compromised due to the added processing of pygame.
    These will be ran after/before the visualization with pygame on the same graphs.
    """

    def __init__():
        pass

    def heuristic_value(x, y):
        (x1, y1) = x
        (x2, y2) = y

        return abs(x1 - x2) + abs(y1 - y2)

    def ida_star():
        return 1

    def save_path(self, vertex, goal):

        if vertex == goal:
            return 1

    def dijkstra(graph, start, goal):
        """A function for finding the shortest path to all vertices from the starting vertix
        using Dijkstra's algorithm.

        Args:
            graph: The graph you want to find the shortest paths in.
            start: The starting node for the algorithm.

        Returns:
            A list of the shortest path to all of the vertices in the graph.
        """

        # Väliaikainen rakenne ennen keon kokoamista itse
        vert = {v: float("inf") for v in range(graph.vertix)}
        vert[start] = 0

        pq = PriorityQueue()
        pq.put((0, start))

        while not pq.empty():
            (null, current) = pq.get()

            graph.seen.append(current)

            for next in range(graph.vertix):
                if graph.edge[current][next] != -1:
                    distance = graph.edge[current][next]
                    if next not in graph.seen:
                        old_cost = vert[next]
                        new_cost = vert[current] + distance
                        if new_cost < old_cost:
                            pq.put((new_cost, next))
                            vert[next] = new_cost
        return vert
