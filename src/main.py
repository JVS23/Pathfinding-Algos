from queue import PriorityQueue


def main():

    class Graph:
        def __init__(self, len_v):
            self.v = len_v
            self.e = [[-1 for i in range(len_v)] for j in range(len_v)]
            self.seen = []

        def add(self, start, end, weight):
            self.e[start][end] = weight
            self.e[end][start] = weight

    def dijkstra(graph, start):
        # Väliaikainen rakenne ennen keon väsäämistä itse
        vert = {v: float("inf") for v in range(graph.v)}
        vert[start] = 0

        pq = PriorityQueue()
        pq.put((0, start))

        while not pq.empty():
            (dist, current) = pq.get()
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

    testGraph = Graph(5)

    testGraph.add(0, 1, 2)
    testGraph.add(0, 2, 1)
    testGraph.add(1, 2, 1)
    testGraph.add(2, 3, 1)
    testGraph.add(3, 4, 6)
    testGraph.add(2, 4, 1)

    print(testGraph.e)

    test_vertex = 0

    x = dijkstra(testGraph, test_vertex)

    print("Dijkstra results for vertex: ", test_vertex, x)


if __name__ == "__main__":
    main()
