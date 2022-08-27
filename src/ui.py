from cgi import test
from graph import Graph
import algorithms
import networkx as nx
import netxfuncs as nxf
import time


def start():

    testGraph = Graph(6)

    testGraph.generate_nodes(6)
    testGraph.generate_edges(6)

    start_vertex = 0
    end_vertex = 5

    nxf.visualize_nx_astar(testGraph.nx_graph, start_vertex, end_vertex)

    """

    





    print("Dijkstras algorithm:")

    # dijkstra_time = time.time()
    dijkstra_result = algorithms.dijkstra(testGraph, start_vertex, end_vertex)

    # print("Dijkstra took:  %s seconds" % (time.time() - dijkstra_time))

    print("\nDijkstra result for vertex ",
          start_vertex, " to ", end_vertex, ": ", dijkstra_result.get(end_vertex), sep="")

    print("\nRoute for NetworkX Dijkstra to node", end_vertex, ":")
    print(nx.dijkstra_path(testGraph.nx_graph, start_vertex, end_vertex), "Length:", (nx.dijkstra_path_length(
        testGraph.nx_graph, start_vertex, end_vertex)))


    print("\nIDA*-algorithm:")

    idastar_time = time.time()
    y = algorithms.ida_star(testGraph, start_vertex, end_vertex)
    print("Ida* took:  %s seconds" % (time.time() - idastar_time))

    print("\nIDA* results for vertex ", end_vertex, ": ", y, sep="")





    """
