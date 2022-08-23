from graph import Graph
import algorithms
import networkx as nx
import netxfuncs as nxf
import time
import ui


def main():

    testGraph = Graph(7)

    testGraph.gen(7)

    start_vertex = 0
    end_vertex = 6

    print("Dijkstras algorithm:")

    dijkstra_time = time.time()
    x = algorithms.dijkstra(testGraph, start_vertex, end_vertex)

    print("Dijkstra took:  %s seconds" % (time.time() - dijkstra_time))

    print("\nDijkstra results for vertex ", start_vertex, ": ", x, sep="")

    print("\nRoute for NetworkX Dijkstra to node", end_vertex, ":")
    print(nx.dijkstra_path(testGraph.nx_graph, start_vertex, end_vertex))

    """
    print("\nIDA*-algorithm:")

    idastar_time = time.time()
    y = algorithms.ida_star(testGraph, start_vertex, end_vertex)
    print("Ida* took:  %s seconds" % (time.time() - idastar_time))

    print("\nIDA* results for vertex ", end_vertex, ": ", y, sep="")
    """

    nxf.visualize_nx_dijkstra(testGraph.nx_graph, start_vertex, end_vertex)


if __name__ == "__main__":
    main()
