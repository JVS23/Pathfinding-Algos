def main():

    # Vain alun pohja suunnittelua varten
    class Graph:
        def __init__(self, len_v):
            self.v = len_v
            self.e = []
            self.seen = []

        def add(self, u, v, weight):
            self.e[u][v] = weight
            self.e[v][u] = weight

        def dijkstra():
            return 0


if __name__ == "__main__":
    main()
