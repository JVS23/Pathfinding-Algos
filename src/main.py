from graph import Graph
import algorithms
import networkx as nx
import netxfuncs as nxf
import time


def main():

    testGraph = Graph(7)

    testGraph.add(0, 1, weight=2)
    testGraph.add(0, 2, weight=1)
    testGraph.add(1, 2, weight=3)
    testGraph.add(2, 3, weight=1)
    testGraph.add(3, 4, weight=6)
    testGraph.add(2, 4, weight=1)
    testGraph.add(1, 4, weight=3)
    testGraph.add(3, 5, weight=2)
    testGraph.add(5, 6, weight=2)
    testGraph.add(4, 6, weight=5)

    G = nx.Graph()

    G.add_edge(0, 1, weight=2)
    G.add_edge(0, 2, weight=1)
    G.add_edge(1, 2, weight=3)
    G.add_edge(2, 3, weight=1)
    G.add_edge(3, 4, weight=6)
    G.add_edge(2, 4, weight=1)
    G.add_edge(1, 4, weight=3)
    G.add_edge(3, 5, weight=2)
    G.add_edge(5, 6, weight=2)
    G.add_edge(4, 6, weight=5)

    start_vertex = 0
    end_vertex = 6

    print("Dijkstras algorithm:")

    dijkstra_time = time.time()
    x = algorithms.dijkstra(testGraph, start_vertex, end_vertex)

    print("Dijkstra took:  %s seconds" % (time.time() - dijkstra_time))

    print("\nDijkstra results for vertex ", start_vertex, ": ", x, sep="")

    print("\nRoute for NetworkX Dijkstra to node", end_vertex, ":")
    print(nx.dijkstra_path(G, start_vertex, end_vertex))

    print("\nIDA*-algorithm:")

    idastar_time = time.time()
    y = algorithms.ida_star(testGraph, start_vertex, end_vertex)
    print("Ida* took:  %s seconds" % (time.time() - idastar_time))

    print("\nIDA* results for vertex ", end_vertex, ": ", y, sep="")

    nxf.visualize_nx_dijkstra(G, start_vertex, end_vertex)

    """

"""


if __name__ == "__main__":
    main()
