class Move:
    def __init__(self, tile, collapsed_value):
        self.tile = tile
        self.possibilities = tile.possibilities
        self.entropy = len(tile.possibilities)
        self.neighbor_possibilities = {}
        self.attempted_collapses = [collapsed_value]
        self.latest_collapsed = collapsed_value
        for direction in tile.neighbors:
            self.neighbor_possibilities[direction] = tile.neighbors[direction].possibilities
    def depleted(self):
        return len(self.attempted_collapses) == len(self.possibilities)