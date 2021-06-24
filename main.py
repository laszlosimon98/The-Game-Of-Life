import pygame
from cell import Cell
pygame.init()

class TheGameOfLife():
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.res = 15 
        self.cols = self.w // self.res
        self.rows = self.h // self.res
        self.win = pygame.display.set_mode((self.w, self.h))
        self.title = pygame.display.set_caption("The Game Of Life")
        self.clock = pygame.time.Clock()
        self.bg = (0,0,0)
        self.grid = self.create2D(self.cols, self.rows)
    
    @staticmethod
    def create2D(cols, rows):
        arr = []
        for i in range(cols):
            arr.append([])
            for j in range(rows):
                arr[i].append([])
        return arr

    def fillGrid(self, cols, rows):
        for i in range(cols):
            for j in range(rows):
                self.grid[i][j] = Cell(i, j, self.res)

    def show(self, win):
        win.fill(self.bg)
        for i in range(self.cols):
            for j in range(self.rows):
                self.grid[i][j].show(win)
        pygame.display.update()

    def updateCell(self):
        update = self.create2D(self.cols, self.rows) 
        for i in range(self.cols):
            for j in range(self.rows):
                update[i][j] = Cell(i, j, self.res) 

        for i in range(self.cols):
            for j in range(self.rows):
                state = self.grid[i][j].isAlive()
                neighbor = self.grid[i][j].countNeighbor(self.grid, self.cols, self.rows, (i, j))

                if not state and neighbor == 3:
                    update[i][j].setState(True)
                elif state and (neighbor < 2 or neighbor > 3):
                    update[i][j].setState(False)
                else:
                    update[i][j].setState(state)
        self.grid = update


    def run(self):
        self.fillGrid(self.cols, self.rows)
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            self.updateCell()
            self.show(self.win)
            self.clock.tick(30)

if __name__ == "__main__":
    game = TheGameOfLife(1200, 700)
    game.run()
