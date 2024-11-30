import random
from Direction import Direction
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
                tile = self.world[y][x]
                if tile.collapsed or tile.entropy < 1:
                    continue
                if tile.entropy < lowest_entropy:
                    lowest_entropy = tile.entropy
                    lowest_entropy_pieces = [tile]
                elif tile.entropy == lowest_entropy:
                    lowest_entropy_pieces.append(tile)
        if len(lowest_entropy_pieces) == 0:
            return None
        return random.choice(lowest_entropy_pieces)
    def collapse(self):
        chosen_tile = self.get_lowest_entropy()
        if chosen_tile is None:
            return
        collapsed_value = random.choice(chosen_tile.possibilities)
        chosen_tile.collapse(collapsed_value)
        queue = list(chosen_tile.neighbors.values())
        visited = set()
        while queue:
            tile = queue.pop(0)
            visited.add(tile)
            new_possibilities = {}
            for direction in tile.neighbors:
                neighbor = tile.neighbors[direction]
                for piece in self.rulebook.pieces:
                    for neighbor_piece in neighbor.get_possibilities():
                        rule = Rule(neighbor_piece, piece, direction)
                        if rule in self.rulebook.rules:
                            if piece not in new_possibilities:
                                new_possibilities[piece] = 0
                            new_possibilities[piece] += 1
                            break
            new_new_possibilities = []
            for i in new_possibilities:
                if new_possibilities[i] == len(tile.neighbors):
                    new_new_possibilities.append(i)
            if sorted(new_new_possibilities) != sorted(tile.possibilities):
                tile.set_possibilities(new_new_possibilities)
                for neighbor in tile.neighbors.values():
                    if neighbor not in visited and not neighbor.collapsed:
                        queue.append(neighbor)