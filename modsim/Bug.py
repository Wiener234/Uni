import pygame
import kruskal
import random

grid = kruskal.Kruskal(6,6)
m = grid.generate()


pygame.init()
screen = pygame.display.set_mode((900,900))
clock = pygame.time.Clock()
running = True

mgridx = 0
mgridy = 0

gridsize = 24

screen.fill("white")

for row in m:
    if row == '\n':
        mgridy += gridsize
        mgridx = 0
        continue
    if row == '#':
        pygame.draw.rect(screen, "black", pygame.Rect(mgridx, mgridy, gridsize, gridsize))

    mgridx += gridsize

srandx = random.randint(1,36)
srandy = random.randint(1,4)


if srandy == 1:
    pygame.draw.rect(screen, "green", pygame.Rect(srandx * gridsize, gridsize, gridsize, gridsize))
elif srandy == 2:
    pygame.draw.rect(screen, "green", pygame.Rect(24*36-gridsize, srandx * gridsize, gridsize, gridsize))
elif srandy == 3:
    pygame.draw.rect(screen, "green", pygame.Rect(srandx * gridsize, 24*36-gridsize, gridsize, gridsize))
elif srandy == 4:
    pygame.draw.rect(screen, "green", pygame.Rect(gridsize, srandx * gridsize, gridsize, gridsize))

srandx = random.randint(1,36)
srandy = random.randint(1,4)


if srandy == 1:
    pygame.draw.rect(screen, "red", pygame.Rect(srandx * gridsize, gridsize, gridsize, gridsize))
elif srandy == 2:
    pygame.draw.rect(screen, "red", pygame.Rect(24*36-gridsize, srandx * gridsize, gridsize, gridsize))
elif srandy == 3:
    pygame.draw.rect(screen, "red", pygame.Rect(srandx * gridsize, 24*36-gridsize, gridsize, gridsize))
elif srandy == 4:
    pygame.draw.rect(screen, "red", pygame.Rect(gridsize, srandx * gridsize, gridsize, gridsize))




while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False





    pygame.display.flip()

    clock.tick(60)

pygame.quit()
