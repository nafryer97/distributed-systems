import copy

class Square:
    ''' represents a 3 by 3 square in the Sudoku Grid '''

    def __init__(self):
        ''' initializes all values with 0, which represents empty boxes '''
        self.square = [[0 for i in range(3)] for j in range(3)]

    def get_row(self,r):
        ''' returns a row of this node's square '''
        return copy.deepcopy(self.square[r])

    def get_col(self,c):
        ''' returns a column from this node's square '''
        return copy.deepcopy([row[c] for row in self.square])

    def assign_val(self,r,c,n):
        ''' assigns a value to a row,col position in the 3x3 square '''
        self.square[r][c]=n

    def get_square(self):
        ''' returns the entire 3x3 square '''
        return copy.deepcopy(self.square)

    def print_square(self):
        '''prints this node's square for debugging '''
        for row in self.square:
            print(row)
        return