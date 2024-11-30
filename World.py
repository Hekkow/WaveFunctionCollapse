import random

from Direction import Direction
from Move import Move
from Rule import Rule
from Tile import Tile
class World:
    def __init__(self, rows, columns, rulebook):
        self.world: list = []
        self.rulebook = rulebook
        self.history = []
        for y in range(rows):
            self.world.append([])
            for x in range(columns):
                self.world[y].append(Tile(x, y, rulebook.pieces))
        for y in range(rows):
            for x in range(columns):
                for direction in Direction:
                    dx, dy = direction.value
                    if 0 <= x + dx < columns and 0 <= y + dy < rows:
                        self.world[y][x].neighbors[direction] = self.world[y+dy][x+dx]
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
    def collapse(self):
        chosen_tile = self.get_lowest_entropy()
        if chosen_tile is None:
            # while True:
            #     move = self.history.pop()
            #     move.tile.undo_collapse(move.possibilities)
            #     for direction in move.tile.neighbors:
            #         move.tile.neighbors[direction].set_possibilities(move.neighbor_possibilities[direction])
            return
        collapsed_value = random.choice(chosen_tile.possibilities)
        move = Move(chosen_tile, collapsed_value)
        chosen_tile.collapse(collapsed_value)

        for direction in chosen_tile.neighbors:
            neighbor = chosen_tile.neighbors[direction]
            for piece in neighbor.possibilities.copy():
                if Rule(piece, chosen_tile.value, direction) not in self.rulebook.rules:
                    neighbor.remove_possibility(piece)
        self.history.append(move)