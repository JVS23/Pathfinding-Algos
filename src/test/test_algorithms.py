
import unittest
import algorithms
from graph import Graph
import networkx


class TestingGraph(unittest.TestCase):

    def setUp(self):
        self.testing_graph = Graph(5)
        self.testing_graph_long = Graph(7)

    def test_generated_graph_dijkstra(self):
        generated_graph = Graph(100)

        generated_graph.generate_nodes(100)
        generated_graph.generate_edges(100)

        dijkstra_result = algorithms.dijkstra(generated_graph, 0, 99)
        nx_result = networkx.dijkstra_path_length(
            generated_graph.nx_graph, 0, 99)

        self.assertEqual(dijkstra_result.get(99),
                         nx_result)

    def test_generated_graph_idastar(self):
        generated_graph = Graph(50)

        generated_graph.generate_nodes(50)
        generated_graph.generate_edges(50)

        idastar_result = algorithms.ida_star(generated_graph, 0, 49)
        nx_result = networkx.dijkstra_path_length(
            generated_graph.nx_graph, 0, 49)

        self.assertEqual(idastar_result,
                         nx_result)


if __name__ == '__main__':
    unittest.main()
