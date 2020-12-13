import copy
import random

class Solver:

    def solve_new_grid(self):
        ''' called when no board was given -- starts making a board '''
        pass

    def solve_given_input(self):
        ''' called when a board was given, check it and start solving '''
        pass
    
    def generate_board(self):
        ''' create a new board from scratch '''
        pass

    def test_board(self,grid):
        ''' tests each box to make sure the solution is valid '''
        pass

    def check_row(self,grid,r,n):
        ''' return True if the number exists in the row '''
        pass

    def check_column(self,grid,c,n):
        ''' returns True if the number exists in the column '''
        pass

    def check_square(self,grid,r,c,n):
        ''' returns True if the number exists in the grid ''' 
        pass
    
    def good_choice(self,grid,r,c,n):
        ''' returns False if the number has been used ''' 
        pass

    def find_empty_box(self,grid):
        ''' returns the next empty box in the board '''
        pass

    def solve_grid(self,grid):
        ''' uses backtracking to solve the board '''
        pass

    def generate_solution(self,grid):
        ''' uses backtracking to generate a solution '''
        pass

    def get_non_empty_boxes(self,grid):
        ''' returns a shuffled list of non-empty boxes in the grid '''
        pass

    def remove_numbers_from_grid(self):
        ''' removes numbers to create a grid with only one solution ''' 
        pass