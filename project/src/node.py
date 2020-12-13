from square import Square as Square
from grid import Grid as Grid
import copy

class Node:
    '''Represents member of the system that's responsible for its own 3x3 square '''
    def __init__(self,pos=0):
        self.pos = pos
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

    
    

