"""
    Module for data structures representing the sudoku board

"""

import copy

class Grid:
    ''' Represents 9 squares together in order as a complete Sudoku grid '''
    def __init__(self,square_list=None,grid=None):
        ''' initializes an empty sudoku grid '''
        self.grid = [[0 for i in range(9)] for j in range(9)]
        self.square_list = [Square() for i in range(9)]

    def get_grid(self):
        ''' returns the list that this instance uses to represent the whole board '''
        return self.grid

    def get_square(self,sq):
        ''' returns the specified 3x3 square out of the 9 total squares '''
        return self.square_list[sq]

    def compile_square_list(self):
        ''' compiles a grid from a list of squares '''
        pass

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

class Square:
    ''' represents a 3 by 3 square in the Sudoku Grid '''

    def __init__(self, square=None):
        ''' initializes all values with 0, which represents empty boxes '''
        self.square = [[0 for i in range(3)] for j in range(3)]

    def get_row(self,r):
        ''' returns a row of this node's square '''
        return self.square[r]

    def get_col(self,c):
        ''' returns a column from this node's square '''
        return [row[c] for row in self.square]
    
    def get_square(self):
        ''' returns the entire 3x3 square '''
        return self.square
    
    def check_num_square(self,num):
        ''' returns true if the number appears in this grid '''
        if any(num in row for row in self.square):
            return True
        return False

    def check_num_row(self,r,n):
        '''returns true if n appears in the row '''
        row = self.get_row(r)
        if n in row:
            return True
        return False

    def check_num_col(self,c,n):
        ''' returns true if n appears in the col '''
        col = self.get_col(c)
        if n in col:
            return True
        return False

    def assign_val(self,r,c,n):
        ''' assigns a value to a row,col position in the 3x3 square '''
        self.square[r][c]=n

    def print_square(self):
        '''prints this node's square for debugging '''
        for row in self.square:
            print(row)
        return
