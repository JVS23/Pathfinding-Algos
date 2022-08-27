from cgi import test
from graph import Graph
import algorithms
import networkx as nx
import netxfuncs as nxf
import time


def start():

    testGraph = Graph(10)

    testGraph.generate_nodes(10)
    testGraph.generate_edges(10)

    start_vertex = 0
    end_vertex = 9

    print("Dijkstras algorithm:")

    dijkstra_time = time.time()
    dijkstra_result = algorithms.dijkstra(testGraph, start_vertex, end_vertex)

    print("Dijkstra took:  %s seconds" % (time.time() - dijkstra_time))

    print("\nDijkstra result for vertex ",
          start_vertex, " to ", end_vertex, ": ", round(dijkstra_result.get(end_vertex), 1), sep="")

    print("\nRoute for NetworkX Dijkstra to node", end_vertex, ":")
    print(nx.dijkstra_path(testGraph.nx_graph, start_vertex, end_vertex), "Length:", round((nx.dijkstra_path_length(
        testGraph.nx_graph, start_vertex, end_vertex)), 1))

    nxf.visualize_nx_astar(testGraph.nx_graph, start_vertex, end_vertex)

    print("\nIDA*-algorithm:")

    idastar_time = time.time()
    y = algorithms.ida_star(testGraph, start_vertex, end_vertex)
    print("IDA* took:  %s seconds" % (time.time() - idastar_time))

    print("\nIDA* results for vertex ", end_vertex, ": ", y, sep="")