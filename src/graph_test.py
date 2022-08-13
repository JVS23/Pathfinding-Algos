
import unittest
import algorithms
from graph import Graph


# Alustava unittestaus, siistitään + tehdään käytännölliseksi kun ehtii


class TestingGraph(unittest.TestCase):

    def setUp(self):
        self.testing_graph = Graph(5)

        self.testing_graph.add(0, 1, 2)
        self.testing_graph.add(0, 2, 1)
        self.testing_graph.add(1, 2, 1)
        self.testing_graph.add(2, 3, 1)
        self.testing_graph.add(3, 4, 6)
        self.testing_graph.add(2, 4, 1)

    def test_premade_graph(self):

        self.assertEqual({0: 0, 1: 2, 2: 1, 3: 2, 4: 2},
                         algorithms.dijkstra(self.testing_graph, 0, 4))


if __name__ == '__main__':
    unittest.main()
