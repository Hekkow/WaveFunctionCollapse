class Tile:
    def __init__(self, x, y, pieces):
        self.x = x
        self.y = y
        self.type = None
        self.possibilities = list(pieces)
        self.entropy = len(pieces)
    def __str__(self):
        if self.type is None:
            return " "
        return self.type
        # s = self.type if self.type is not None else ''.join(self.possibilities)
        # s += ' '*(3-len(s))
        # return f"[{s}]"
        # return f"[{self.x},{self.y} {self.entropy}]"
    def remove_possibility(self, piece):
        self.possibilities.remove(piece)
        self.entropy -= 1