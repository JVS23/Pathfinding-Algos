from graph import Graph
from algorithms import Algos


def main():

    testGraph = Graph(5)

    testGraph.add(0, 1, 2)
    testGraph.add(0, 2, 1)
    testGraph.add(1, 2, 1)
    testGraph.add(2, 3, 1)
    testGraph.add(3, 4, 6)
    testGraph.add(2, 4, 1)

    test_vertex = 0

    x = Algos.dijkstra(testGraph, test_vertex)

    print("Dijkstra results for vertex ", test_vertex, ": ", x, sep="")


if __name__ == "__main__":
    main()
