from graph import Graph
from algorithms import Algos
import networkx as nx
import netxfuncs as nxf


def main():

    testGraph = Graph(5)

    testGraph.add(0, 1, 2)
    testGraph.add(0, 2, 1)
    testGraph.add(1, 2, 1)
    testGraph.add(2, 3, 1)
    testGraph.add(3, 4, 6)
    testGraph.add(2, 4, 1)

    G = nx.Graph()
    G.add_edge(0, 1, weight=2)
    G.add_edge(0, 2, weight=1)
    G.add_edge(1, 2, weight=1)
    G.add_edge(2, 3, weight=1)
    G.add_edge(3, 4, weight=6)
    G.add_edge(2, 4, weight=1)

    start_vertex = 0
    end_vertex = 4

    x = Algos.dijkstra(testGraph, start_vertex, end_vertex)

    print("\nDijkstra results for vertex ", start_vertex, ": ", x, sep="")

    print("\nRoute for NetworkX Dijkstra to node", end_vertex, ":")
    print(nx.dijkstra_path(G, start_vertex, end_vertex))
    nxf.visualize_nx_dijkstra(G, start_vertex, end_vertex)

    print("Route for NetworkX A* to node", end_vertex, ":")
    print(nx.astar_path(G, start_vertex, end_vertex))
    nxf.visualize_nx_astar(G, start_vertex, end_vertex)


if __name__ == "__main__":
    main()
