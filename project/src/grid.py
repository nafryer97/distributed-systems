import copy

class Grid:
    ''' Represents 9 squares together in order as a complete Sudoku grid '''
    def __init__(self):
        ''' initializes an empty sudoku grid '''
        self.grid = [[0 for i in range(9)] for j in range(9)]

    def get_grid(self):
        return self.grid

    def compile_grid(self,sq0,sq1,sq2,sq3,sq4,sq5,sq6,sq7,sq8):
        ''' compiles a sudoku grid from 9 squares '''
        for i in range(3):
            self.grid[i] = sq0[i] + sq1[i] + sq2[i]
        for i in range(3):
            self.grid[i+3] = sq3[i] + sq4[i] + sq5[i]
        for i in range(3):
            self.grid[i+6] = sq6[i] + sq7[i] + sq8[i]

    def check_grid(self):
        ''' checks to see if the grid is a solution '''
        pass

    def create_grid(self):
        ''' creates a new sudoku grid with one solution '''
        pass

    def get_square(self,sq):
        ''' returns the specified 3x3 square out of the 9 total squares '''
        pass
