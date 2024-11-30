from Rule import Rule


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
        # if self.value is None:
        #     if self.possibilities:
        #         return str(self.possibilities)
        #     else:
        #         return "EMPTY"
        # return self.value
        return str(self.get_possibilities())
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
    # def update_possibilities(self, rulebook):
    #     new_possibilities = {}
    #     for direction in self.neighbors:
    #         neighbor = self.neighbors[direction]
    #         values = neighbor.possibilities.copy()
    #         if neighbor.collapsed:
    #             values = [neighbor.value]
    #         for value in values:
    #             for possibility in self.possibilities:
    #                 # print(self.x, self.y, Rule(value, possibility, direction))
    #                 if Rule(value, possibility, direction) in rulebook.rules:
    #                     if value not in new_possibilities:
    #                         new_possibilities[value] = 0
    #                     new_possibilities[value] += 1
    #                     # self.remove_possibility(possibility)
    #     print(new_possibilities)
    #     # self.possibilities = new_possibilities
    #     # self.entropy = len(new_possibilities)

    def update_neighbors(self, rulebook):
        for direction in self.neighbors:
            neighbor = self.neighbors[direction]
            self_values = self.possibilities
            if self.collapsed:
                self_values = self.value
            new_neighbor_possibilities = []
            for neighbor_possibility in neighbor.possibilities.copy():
                for self_value in self_values:
                    if Rule(neighbor_possibility, self_value, direction) in rulebook.rules:
                        new_neighbor_possibilities.append(neighbor_possibility)
                        print(self.value, self.x, self.y, Rule(neighbor_possibility, self_value, direction), neighbor.x, neighbor.y)
                        # neighbor.remove_possibility(neighbor_possibility)
            if new_neighbor_possibilities != neighbor.possibilities:
                neighbor.possibilities = new_neighbor_possibilities
                neighbor.update_neighbors(rulebook)
    def get_possibilities(self):
        if self.collapsed:
            return self.value
        return self.possibilities