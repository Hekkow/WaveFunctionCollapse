from Direction import Direction
from Rule import Rule


class Rulebook:
    def __init__(self, image):
        self.pieces = set()
        self.rules = set()
        for y in range(len(image)):
            for x in range(len(image[y])):
                self.pieces.add(image[y][x])
                if x + 1 < len(image[y]):
                    self.rules.add(Rule(image[y][x], image[y][x + 1], Direction.RIGHT))
                if x - 1 >= 0:
                    self.rules.add(Rule(image[y][x], image[y][x - 1], Direction.LEFT))
                if y + 1 < len(image):
                    self.rules.add(Rule(image[y][x], image[y + 1][x], Direction.DOWN))
                if y - 1 >= 0:
                    self.rules.add(Rule(image[y][x], image[y - 1][x], Direction.UP))