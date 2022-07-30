from queue import PriorityQueue


class Algos():

    def __init__():
        pass

    def dijkstra(graph, start):
        """A function for finding the shortest path to all vertices from the starting vertix
        using Dijkstra's algorithm.

        Args:
            graph: The graph you want to find the shortest paths in.
            start: The starting node for the algorithm.

        Returns:
            A list of the shortest path to all of the vertices in the graph.
        """

        # Väliaikainen rakenne ennen keon kokoamista itse
        vert = {v: float("inf") for v in range(graph.v)}
        vert[start] = 0

        pq = PriorityQueue()
        pq.put((0, start))

        while not pq.empty():
            (null, current) = pq.get()

            graph.seen.append(current)

            for next in range(graph.v):
                if graph.e[current][next] != -1:
                    distance = graph.e[current][next]
                    if next not in graph.seen:
                        old_cost = vert[next]
                        new_cost = vert[current] + distance
                        if new_cost < old_cost:
                            pq.put((new_cost, next))
                            vert[next] = new_cost
        return vert
