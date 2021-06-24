import pygame
import random
pygame.font.init()

class Cell():
    def __init__(self, i, j, r, fill=True):
        self.i = i
        self.j = j
        self.r = r
        self.alive = True if random.random() > 0.5 else False

    def show(self, win):
        x = self.i*self.r
        y = self.j*self.r
        if self.alive:
            pygame.draw.rect(win, (255,255,255), (x, y, self.r-1, self.r-1))
        else:
            pygame.draw.rect(win, (0,0,0), (x, y, self.r-1, self.r-1))

    def countNeighbor(self, grid, cols, rows, pos):
        x = pos[0]
        y = pos[1]
        neighbor = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                col = (x + i + cols) % cols
                row = (y + j + rows) % rows 
                if grid[col][row].isAlive():
                    neighbor += 1
        if grid[x][y].isAlive():
            neighbor -= 1
        
        return neighbor
    
    def isAlive(self):
        return self.alive

    def setState(self, state):
        self.alive = state
