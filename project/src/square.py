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
    
    def get_square(self):
        ''' returns the entire 3x3 square '''
        return copy.deepcopy(self.square)
    
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