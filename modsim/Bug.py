import pygame
import numpy as np
from numpy.random import shuffle
import random

from mazelib import Maze
from mazelib.generate.Kruskal import Kruskal

m = Maze()
m.generator = Kruskal(18, 18)
m.generate()
print(m.tostring(True))

pygame.init()
screen = pygame.display.set_mode((900,900))
clock = pygame.time.Clock()
running = True

mgridx = 0
mgridy = 0

gridsize = 24

# for row in m.tostring():
#     for cell in row:
#         if cell == '#': 
#             pygame.draw.rect(screen, "white", pygame.Rect(mgridx, mgridy, gridsize, gridsize))
#         else: 
#             pygame.draw.rect(screen, "black", pygame.Rect(mgridx, mgridy, gridsize, gridsize))
#         mgridx += gridsize
#     mgridx = 0
#     mgridy += gridsize
i = 0

screen.fill("white")

for row in m.tostring(True):
    if row == '\n':
        mgridy += gridsize
        mgridx = 0
        continue
    if row == '#':
        pygame.draw.rect(screen, "black", pygame.Rect(mgridx, mgridy, gridsize, gridsize))

    mgridx += gridsize

srandx = random.randint(1,37)
srandy = random.randint(1,5)


if srandy == 1:
    pygame.draw.rect(screen, "green", pygame.Rect(srandx * gridsize, gridsize, gridsize, gridsize))
elif srandy == 2:
    pygame.draw.rect(screen, "green", pygame.Rect(24*36-gridsize, srandx * gridsize, gridsize, gridsize))
elif srandy == 3:
    pygame.draw.rect(screen, "green", pygame.Rect(srandx * gridsize, 24*36-gridsize, gridsize, gridsize))
elif srandy == 4:
    pygame.draw.rect(screen, "green", pygame.Rect(gridsize, srandx * gridsize, gridsize, gridsize))




while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False





    # create start and finish 
    # pygame.draw.rect(screen, "green", pygame.Rect(0, 0, 50, 50))
    # pygame.draw.rect(screen, "red", pygame.Rect(850, 850, 50, 50))



    # creates a grid mazexxmazex with 324 squares
    # for i in range(50, screen.get_width(), 50):
        # pygame.draw.line(screen, "black", pygame.Vector2(i,0), (i,900), 2)
        # pygame.draw.line(screen, "black", pygame.Vector2(0,i), (900,i), 2)

    # draw maze boarder
    # pygame.draw.lines(screen, "black", True, [(0,0), (0,898), (898,898), (898,0)], 2)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
