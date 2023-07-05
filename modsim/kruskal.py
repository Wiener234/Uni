import numpy as np
from numpy.random import shuffle

class Kruskal:
    def __init__(self, h, w):
        self.H = 2*h+1
        self.W = 2*w+1
    
    
    def generate(self):
        grid = np.empty((self.H,self.W), dtype=np.int8) # create np.array 
        grid.fill(1)                                    # fill array with 1
        
        forest = []
        for row in range(1,self.H-1, 2):
            for col in range(1,self.W-1, 2):
                forest.append([(row,col)])
                grid[row][col] = 0
        
        edges = []
        for row in range(2, self.H-1, 2):
            for col in range (1,self.W-1, 2):
                edges.append((row,col))
        for row in range(1, self.H-1, 2):
            for col in range (2,self.W-1, 2):
                edges.append((row,col))
        
        shuffle(edges)
        
        while len(forest) > 1:
            ce_row, ce_col = edges[0]
            edges = edges[1:]
        
            tree1 = -1
            tree2 = -1
        
            if ce_row % 2 == 0:
                tree1 = sum(
                        [
                            i if (ce_row - 1, ce_col) in j else 0
                            for i,j in enumerate(forest)
                        ]
                    )
                tree2 = sum(
                        [
                            i if (ce_row + 1, ce_col) in j else 0
                            for i,j in enumerate(forest)
                        ]
                    )
            else:
                tree1 = sum(
                        [
                            i if (ce_row, ce_col - 1) in j else 0
                            for i,j in enumerate(forest)
                        ]
                    )
                tree2 = sum(
                        [
                            i if (ce_row, ce_col + 1) in j else 0
                            for i,j in enumerate(forest)
                        ]
                    )
            if tree1 != tree2:
                new_tree = forest[tree1] + forest[tree2]
                temp1 = list(forest[tree1])
                temp2 = list(forest[tree2])
                forest = [
                        x for x in forest if x != temp1
                        ]
                forest = [x for x in forest if x != temp2]
                forest.append(new_tree)
                grid[ce_row][ce_col] = 0
        
        txt = []
        for row in grid:
            txt.append("".join(["#" if cell else " " for cell in row]))
        return "\n".join(txt)
