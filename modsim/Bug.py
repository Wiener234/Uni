# import pygame
import kruskal
import random
import numpy as np
import csv

fields = ["Iteration", "Size", "Iteration of Size", "Time", "Steps", "Maze", "Order of Steps"]

row = []
up = "up"
down = "down"
left = "left"
right = "right"

iter = 0
for i in range(3, 11):
    j = 0
    L = []
    while j < 100:
        iter += 1
        j += 1
        x = i
        y = i
        
        grid = kruskal.Kruskal(x,y)
        mar = grid.generate()
        # m = grid.out()
        # np.savetxt("test", mar, fmt="%1d")
        
        
        start = [2,2]
        end = [x*2,y*2]
        bug = start
        
        time = 0
        steps = 0
        
        turns = []
        while end != bug:
            turn = random.randint(0,3)
         
            #move
            if turn == 0:
                if mar[bug[0]][bug[1]+1] == 0 and mar[bug[0]][bug[1]+2] == 0: #right
                    bug = [bug[0], bug[1]+2]
                    time += 1
                    turns.append([turn, right])
                elif mar[bug[0]+1][bug[1]] == 0 and mar[bug[0]+2][bug[1]] == 0: #down
                    bug = [bug[0]+2, bug[1]]
                    time += 2
                    turns.append([turn, down])
                elif mar[bug[0]][bug[1]-1] == 0 and mar[bug[0]][bug[1]-2] == 0: #left
                    bug = [bug[0], bug[1]-2]
                    time += 3
                    turns.append([turn, left])
                elif mar[bug[0]-1][bug[1]] == 0 and mar[bug[0]-2][bug[1]] == 0: #up
                    bug = [bug[0]-2, bug[1]]
                    time += 4
                    turns.append([turn, right])
            elif turn == 1:
                if mar[bug[0]+1][bug[1]] == 0 and mar[bug[0]+2][bug[1]] == 0: #down
                    bug = [bug[0]+2, bug[1]]
                    time += 1
                    turns.append([turn, down])
                elif mar[bug[0]][bug[1]-1] == 0 and mar[bug[0]][bug[1]-2] == 0: #left
                    bug = [bug[0], bug[1]-2]
                    time += 2
                    turns.append([turn, left])
                elif mar[bug[0]-1][bug[1]] == 0 and mar[bug[0]-2][bug[1]] == 0: #up
                    bug = [bug[0]-2, bug[1]]
                    time += 3
                    turns.append([turn, up])
                elif mar[bug[0]][bug[1]+1] == 0 and mar[bug[0]][bug[1]+2] == 0: #right
                    bug = [bug[0], bug[1]+2]
                    time += 4
                    turns.append([turn, right])
            elif turn == 2:
                if mar[bug[0]][bug[1]-1] == 0 and mar[bug[0]][bug[1]-2] == 0: #left
                    bug = [bug[0], bug[1]-2]
                    time += 1
                    turns.append([turn, left])
                elif mar[bug[0]-1][bug[1]] == 0 and mar[bug[0]-2][bug[1]] == 0: #up
                    bug = [bug[0]-2, bug[1]]
                    time += 2
                    turns.append([turn, up])
                elif mar[bug[0]][bug[1]+1] == 0 and mar[bug[0]][bug[1]+2] == 0: #right
                    bug = [bug[0], bug[1]+2]
                    time += 3
                    turns.append([turn, right])
                elif mar[bug[0]+1][bug[1]] == 0 and mar[bug[0]+2][bug[1]] == 0: #down
                    bug = [bug[0]+2, bug[1]]
                    time += 4
                    turns.append([turn, down])
            elif turn == 3:
                if mar[bug[0]-1][bug[1]] == 0 and mar[bug[0]-2][bug[1]] == 0: #up
                    bug = [bug[0]-2, bug[1]]
                    time += 1
                    turns.append([turn, up])
                elif mar[bug[0]][bug[1]+1] == 0 and mar[bug[0]][bug[1]+2] == 0: #right
                    bug = [bug[0], bug[1]+2]
                    time += 2
                    turns.append([turn, right])
                elif mar[bug[0]+1][bug[1]] == 0 and mar[bug[0]+2][bug[1]] == 0: #down
                    bug = [bug[0]+2, bug[1]]
                    time += 3
                    turns.append([turn, down])
                elif mar[bug[0]][bug[1]-1] == 0 and mar[bug[0]][bug[1]-2] == 0: #left
                    bug = [bug[0], bug[1]-2]
                    time += 4
                    turns.append([turn, left])
         
            steps += 1
        L.append({'Iteration' : iter, 'Size' : i,'Iteration of Size' : j, 'Time' : time, 'Steps' : steps, 'Order of Steps' : turns,'Maze' : mar})
        row.append(L)


    
    



    filename = "modsim_0.1_" + str(i) + ".csv"
    with open(filename, 'w', newline="") as csvfile:
        csvwrite = csv.DictWriter(csvfile, fieldnames=fields)
        csvwrite.writeheader()
        for _row in row:
            for _col in _row:
                csvwrite.writerow(_col)
    row = []








#pygame.init()
#screen = pygame.display.set_mode((900,900))
#clock = pygame.time.Clock()
#running = True

#mgridx = 0
#mgridy = 0

#gridsize = 24





#while running:
#    for event in pygame.event.get():
#        if event.type == pygame.QUIT:
#            running = False

#    #grid
#    screen.fill("white")
    
#    for row in m:
#        if row == '\n':
#            mgridy += gridsize
#            mgridx = 0
#            continue
#        if row == '#':
#            pygame.draw.rect(screen, "black", pygame.Rect(mgridx, mgridy, gridsize, gridsize))
    
#        mgridx += gridsize
#    mgridx = 0
#    mgridy = 0

#    turn = random.randint(0,3)
#    # move
#    if turn == 0:
#        if mar[bug[0]][bug[1]+1] == 0 and mar[bug[0]][bug[1]+2] == 0: #right
#            bug = [bug[0], bug[1]+2]
#            time += 1
#        elif mar[bug[0]+1][bug[1]] == 0 and mar[bug[0]+2][bug[1]] == 0: #down
#            bug = [bug[0]+2, bug[1]]
#            time += 2
#        elif mar[bug[0]][bug[1]-1] == 0 and mar[bug[0]][bug[1]-2] == 0: #left
#            bug = [bug[0], bug[1]-2]
#            time += 3
#        elif mar[bug[0]-1][bug[1]] == 0 and mar[bug[0]-2][bug[1]] == 0: #up
#            bug = [bug[0]-2, bug[1]]
#            time += 4
#    elif turn == 1:
#        if mar[bug[0]+1][bug[1]] == 0 and mar[bug[0]+2][bug[1]] == 0: #down
#            bug = [bug[0]+2, bug[1]]
#            time += 1
#        elif mar[bug[0]][bug[1]-1] == 0 and mar[bug[0]][bug[1]-2] == 0: #left
#            bug = [bug[0], bug[1]-2]
#            time += 2
#        elif mar[bug[0]-1][bug[1]] == 0 and mar[bug[0]-2][bug[1]] == 0: #up
#            bug = [bug[0]-2, bug[1]]
#            time += 3
#        elif mar[bug[0]][bug[1]+1] == 0 and mar[bug[0]][bug[1]+2] == 0: #right
#            bug = [bug[0], bug[1]+2]
#            time += 4
#    elif turn == 2:
#        if mar[bug[0]][bug[1]-1] == 0 and mar[bug[0]][bug[1]-2] == 0: #left
#            bug = [bug[0], bug[1]-2]
#            time += 1
#        elif mar[bug[0]-1][bug[1]] == 0 and mar[bug[0]-2][bug[1]] == 0: #up
#            bug = [bug[0]-2, bug[1]]
#            time += 2
#        elif mar[bug[0]][bug[1]+1] == 0 and mar[bug[0]][bug[1]+2] == 0: #right
#            bug = [bug[0], bug[1]+2]
#            time += 3
#        elif mar[bug[0]+1][bug[1]] == 0 and mar[bug[0]+2][bug[1]] == 0: #down
#            bug = [bug[0]+2, bug[1]]
#            time += 4
#    elif turn == 3:
#        if mar[bug[0]-1][bug[1]] == 0 and mar[bug[0]-2][bug[1]] == 0: #up
#            bug = [bug[0]-2, bug[1]]
#            time += 1
#        elif mar[bug[0]][bug[1]+1] == 0 and mar[bug[0]][bug[1]+2] == 0: #right
#            bug = [bug[0], bug[1]+2]
#            time += 2
#        elif mar[bug[0]+1][bug[1]] == 0 and mar[bug[0]+2][bug[1]] == 0: #down
#            bug = [bug[0]+2, bug[1]]
#            time += 3
#        elif mar[bug[0]][bug[1]-1] == 0 and mar[bug[0]][bug[1]-2] == 0: #left
#            bug = [bug[0], bug[1]-2]
#            time += 4
    
#    steps += 1


#    # start finish
#    pygame.draw.rect(screen, "green", pygame.Rect(start[0] * gridsize, start[1] * gridsize, gridsize, gridsize))
#    pygame.draw.rect(screen, "red", pygame.Rect(end[0] * gridsize, end[1] * gridsize, gridsize, gridsize))
  

#    #bug
#    pygame.draw.rect(screen, "magenta", pygame.Rect(bug[1] * gridsize, bug[0] * gridsize, gridsize, gridsize))



#    pygame.display.flip()
#    if bug == end:
#        running = False

#    clock.tick(100000)

#pygame.quit()
