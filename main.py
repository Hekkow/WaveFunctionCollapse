import random

from Direction import Direction
from Rule import Rule
from World import World
rows = 9
cols = 20

image = ["SSS",
         "CCS",
         "LLC",
         "LLL"]
# image = [["S", "S", "S"],
#          ["C", "C", "S"],
#          ["L", "L", "C"],
#          ["L", "L", "L"]]


rules = set()
pieces = set()

for y in range(len(image)):
    for x in range(len(image[y])):
        pieces.add(image[y][x])
        if x+1 < len(image[y]):
            rules.add(Rule(image[y][x], image[y][x + 1], Direction.RIGHT))
        if x-1 >= 0:
            rules.add(Rule(image[y][x], image[y][x - 1], Direction.LEFT))
        if y+1 < len(image):
            rules.add(Rule(image[y][x], image[y + 1][x], Direction.DOWN))
        if y-1 >= 0:
            rules.add(Rule(image[y][x], image[y - 1][x], Direction.UP))

print(rules)

world = World(rows, cols, pieces)
print(world)
for i in range(rows*cols):
    chosen_tile = world.get_lowest_entropy()
    if chosen_tile is None:
        break
    chosen_tile.type = random.choice(chosen_tile.possibilities)
    chosen_tile.possibilities = []
    chosen_tile.entropy = -1
    for direction in Direction:
        x, y = chosen_tile.x, chosen_tile.y
        dx, dy = direction.value
        if 0 <= chosen_tile.x + dx < len(world.world[0]) and 0 <= chosen_tile.y + dy < len(world.world):
            tile = world.world[y+dy][x+dx]
            for piece in tile.possibilities.copy():
                if Rule(piece, chosen_tile.type, (-dx, -dy)) not in rules:
                    tile.remove_possibility(piece)
    print(world)

# wor

# grid = Grid([[0, 0, 0, 0],
#              [0, 1, 1, 0],
#              [0, 1, 1, 0],
#              [0, 0, 0, 0]])

# manually add each connection and possible left/right/up/down tiles

# pieces = [Piece(0, [1, 0], [1, 0], [1, 0], [1, 0])]

# world = World(rows, cols)
# # print(grid.valid_neighbors(1, 1, 0))
#
# print(world)