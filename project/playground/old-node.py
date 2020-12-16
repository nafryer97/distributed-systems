from square import Square as Square
from grid import Grid as Grid
import copy

class Node:
    '''Represents member of the system that's responsible for its own 3x3 square '''
    def __init__(self,pos=0):
        self.pos = pos
        self.path = 0
        self.square = Square()

    def get_position(self):
        ''' returns this node's position on the board as one of 0-8 '''
        return self.pos

    def get_square(self):
        ''' calls the Square.get_getsquare() method '''
        return self.square.get_square()

    def get_row(self,r):
        ''' calls the Square.get_row() method '''
        return self.square.get_row(r)

    def get_col(self,c):
        ''' calls the Square.get_col() method '''
        return self.square.get_col(c)

    def check_num_node(self,n):
        ''' returns true if this node has that number '''
        return self.square.check_num_square(n)

    def check_row_node(self,r,n):
        ''' returns true if the number is in the row for this node '''
        return self.square.check_num_row(r,n)

    def check_col_node(self,c,n):
        ''' returns true if the number is in the col for this node '''
        return self.square.check_num_col(c,n)

    

class NodeZero(Node):
    ''''''
    def good_choice(self,r,c,n):
        ''''''
        pass
    def solve_row(self,row):
        ''' fills in values for a row '''
        pass

    def generate_row(self,r):
        ''''''
        pass

class NodeOne(Node):
    ''''''
    pass

class NodeTwo(Node):
    ''''''
    pass

class NodeThree(Node):
    ''''''
    pass

class NodeFour(Node):
    ''''''
    pass

class NodeFive(Node):
    pass

class NodeSix(Node):
    pass

class NodeSeven(Node):
    pass

class NodeEight(Node):
    pass