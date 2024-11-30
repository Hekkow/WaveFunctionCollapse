class Tile:

    def __init__(self, x, y, pieces):
        self.x = x
        self.y = y
        self.neighbors = {}
        self.value = None
        self.possibilities = list(pieces)
        self.entropy = len(pieces)
        self.collapsed = False
    def __str__(self):
        if self.value is None:
            if self.possibilities:
                return str(self.possibilities)
            else:
                return "EMPTY"
        return self.value
    def remove_possibility(self, piece):
        self.possibilities.remove(piece)
        self.entropy -= 1
    def set_possibilities(self, possibilities):
        self.possibilities = list(possibilities)
        self.entropy = len(self.possibilities)
    def collapse(self, value):
        self.value = value
        self.possibilities = []
        self.entropy = 0
        self.collapsed = True
    def undo_collapse(self, possibilities):
        self.value = None
        self.set_possibilities(possibilities)
        self.collapsed = False