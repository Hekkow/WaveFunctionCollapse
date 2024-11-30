import pygame
from Direction import Direction
from Rule import Rule
from Rulebook import Rulebook
from World import World
rows = 9
cols = 20
pygame.init()
text_font = pygame.font.SysFont('Arial', 12)
screen = pygame.display.set_mode((1600, 900))
fps = 60
clock = pygame.time.Clock()

image = ["SSS",
         "CCS",
         "LLC",
         "LLL"]

rulebook = Rulebook(image)

world = World(rows, cols, rulebook)
box_size = 70
padding = 1
box_with_padding = box_size + padding

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
                    box_color = (0, 255, 0)
                case "S":
                    box_color = (0, 0, 255)
                case "C":
                    box_color = (255, 255, 0)
            text_color = (0, 0, 0)
            text_surface = text_font.render(str(tile.possibilities), False, text_color)
            pygame.draw.rect(screen, box_color, pygame.Rect(box_with_padding*j, height-box_with_padding*i, box_size, box_size))
            screen.blit(text_surface, (box_with_padding*j, height-box_with_padding*i))
    pygame.display.flip()
    clock.tick(fps)