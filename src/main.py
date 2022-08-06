from graph import Graph
from algorithms import Algos
import pygame
import sys

BLACK = (0, 0, 0)
WHITE = (250, 250, 250)
GOALGREEN = (0, 255, 0)
STARTBLUE = (0, 0, 255)

HEIGHTWIDTH = 700
WINDOW = pygame.display.set_mode((HEIGHTWIDTH, HEIGHTWIDTH))
pygame.display.set_caption("AlgoGrid")


def create_grid():
    grid_size = 20
    for x in range(0, HEIGHTWIDTH, grid_size):
        for y in range(0, HEIGHTWIDTH, grid_size):
            rect = pygame.Rect(x, y, grid_size, grid_size)
            pygame.draw.rect(SCREEN, BLACK, rect, 1)


def main(WINDOW, HEIGHTWIDTH):
    global SCREEN
    SCREEN = pygame.display.set_mode((HEIGHTWIDTH, HEIGHTWIDTH))
    SCREEN.fill(WHITE)

    testGraph = Graph(5)

    testGraph.add(0, 1, 2)
    testGraph.add(0, 2, 1)
    testGraph.add(1, 2, 1)
    testGraph.add(2, 3, 1)
    testGraph.add(3, 4, 6)
    testGraph.add(2, 4, 1)

    start_vertex = 0

    x = Algos.dijkstra(testGraph, start_vertex)

    print("Dijkstra results for vertex ", start_vertex, ": ", x, sep="")

    while True:
        create_grid()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()


if __name__ == "__main__":
    main(WINDOW, HEIGHTWIDTH)
