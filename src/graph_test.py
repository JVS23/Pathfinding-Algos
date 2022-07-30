import unittest
from graph import Graph
from algorithms import Algos

# Alustava unittestaus, siistitään + tehdään käytännölliseksi ensipalautukseen


class TestingGraph(unittest.TestCase):

    def test_graph(self):
        testing_graph = Graph(5)

        testing_graph.add(0, 1, 2)
        testing_graph.add(0, 2, 1)
        testing_graph.add(1, 2, 1)
        testing_graph.add(2, 3, 1)
        testing_graph.add(3, 4, 6)
        testing_graph.add(2, 4, 1)

        self.assertEqual({0: 0, 1: 2, 2: 1, 3: 2, 4: 2},
                         Algos.dijkstra(testing_graph, 0))


if __name__ == '__main__':
    unittest.main()
