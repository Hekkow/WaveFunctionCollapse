import random

from Tile import Tile
class World:
    world = []
    def __init__(self, rows, columns, pieces):
        for y in range(rows):
            self.world.append([])
            for x in range(columns):
                self.world[y].append(Tile(x, y, pieces))

    def __str__(self):
        string = ""
        for y in self.world:
            for x in y:
                string += str(x) + " "
            string += "\n"
        return string
    def get_lowest_entropy(self):
        lowest_entropy = 1000
        lowest_entropy_pieces = []
        for y in range(len(self.world)):
            for x in range(len(self.world[y])):
                if self.world[y][x].entropy < 1:
                    continue
                if self.world[y][x].entropy < lowest_entropy:
                    lowest_entropy = self.world[y][x].entropy
                    lowest_entropy_pieces = [self.world[y][x]]
                elif self.world[y][x].entropy == lowest_entropy:
                    lowest_entropy_pieces.append(self.world[y][x])
        if len(lowest_entropy_pieces) == 0:
            return None
        return random.choice(lowest_entropy_pieces)