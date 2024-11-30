import pygame
from Rulebook import Rulebook
from World import World

rows = 40
cols = 40

sea_color = (61, 176, 252)
coast_color = (252, 211, 61)
land_color = (179, 252, 61)

box_size = 20
padding = 0
box_with_padding = box_size + padding

image = ["LLLLLL",
         "LCCCCL",
         "LCSSCL",
         "LCSSCL",
         "LCCCCL",
         "LLLLLL",
         ]

image = ["LLLLCLLL",
         "LLLCSCLL",
         "LLCSSCCL",
         "LLLCCCLL",
         "LLLLLLLL",]
#
image = ["LLL",
         "LLC",
         "CCC",
         "CCS",
         "SSS",]

rulebook = Rulebook(image)
world = World(rows, cols, rulebook)

fps = 240
clock = pygame.time.Clock()
pygame.init()
text_font = pygame.font.SysFont('Arial', 12)
screen = pygame.display.set_mode((1600, 900))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    world.collapse()
    height = rows * box_size
    for i in range(rows):
        for j in range(cols):
            tile = world.world[i][j]
            box_color = (255, 255, 255)
            match tile.value:
                case "L":
                    box_color = land_color
                case "S":
                    box_color = sea_color
                case "C":
                    box_color = coast_color
            pygame.draw.rect(screen, box_color, pygame.Rect(box_with_padding * j, height - box_with_padding * i, box_size, box_size))
            # text_color = (0, 0, 0)
            # text_surface = text_font.render(f"{tile.x},{tile.y} {tile}", False, text_color)
            # screen.blit(text_surface, (box_with_padding*j, height-box_with_padding*i))
    pygame.display.flip()
    clock.tick(fps)