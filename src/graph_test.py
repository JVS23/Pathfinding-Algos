
import unittest
import algorithms
from graph import Graph


# Alustava unittestaus, siistitään + tehdään käytännölliseksi kun ehtii


class TestingGraph(unittest.TestCase):

    def setUp(self):
        self.testing_graph = Graph(5)
        self.testing_graph_long = Graph(7)

        self.testing_graph.add(0, 1, 2)
        self.testing_graph.add(0, 2, 1)
        self.testing_graph.add(1, 2, 1)
        self.testing_graph.add(2, 3, 1)
        self.testing_graph.add(3, 4, 6)
        self.testing_graph.add(2, 4, 1)

        self.testing_graph_long.add(0, 1, weight=2)
        self.testing_graph_long.add(0, 2, weight=1)
        self.testing_graph_long.add(1, 2, weight=3)
        self.testing_graph_long.add(2, 3, weight=1)
        self.testing_graph_long.add(3, 4, weight=6)
        self.testing_graph_long.add(2, 4, weight=1)
        self.testing_graph_long.add(1, 4, weight=3)
        self.testing_graph_long.add(3, 5, weight=2)
        self.testing_graph_long.add(5, 6, weight=2)
        self.testing_graph_long.add(4, 6, weight=5)

    def test_premade_graph(self):

        self.assertEqual({0: 0, 1: 2, 2: 1, 3: 2, 4: 2},
                         algorithms.dijkstra(self.testing_graph, 0, 4))


if __name__ == '__main__':
    unittest.main()
