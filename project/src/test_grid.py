from grid import Grid as Grid
import unittest
import random

class InitTest(unittest.TestCase):
    ''' tests the initialization of an empty grid '''
    def test_init(self):
        empty_grid = [[0 for i in range(9)] for j in range(9)]
        g = Grid()
        self.assertEqual(g.get_grid(),empty_grid)

class CompileGridTest(unittest.TestCase):
    ''' tests the compile grid with 9 random squares '''
    
    def test_compile(self):
        ''' generates a random 9 x 9 grid and then passes 3 x 3 segments of it to the compile method '''
        rand_grid = [[random.randint(1,9) for i in range(9)] for j in range(9)]
        g = Grid()
        sq0 = [[rand_grid[j][i] for i in range(0,3)] for j in range(0,3)]
        sq1 = [[rand_grid[j][i] for i in range(3,6)] for j in range(0,3)]
        sq2 = [[rand_grid[j][i] for i in range(6,9)] for j in range(0,3)]
        sq3 = [[rand_grid[j][i] for i in range(0,3)] for j in range(3,6)]
        sq4 = [[rand_grid[j][i] for i in range(3,6)] for j in range(3,6)]
        sq5 = [[rand_grid[j][i] for i in range(6,9)] for j in range(3,6)]
        sq6 = [[rand_grid[j][i] for i in range(0,3)] for j in range(6,9)]
        sq7 = [[rand_grid[j][i] for i in range(3,6)] for j in range(6,9)]
        sq8 = [[rand_grid[j][i] for i in range(6,9)] for j in range(6,9)]

        g.compile_grid(sq0,sq1,sq2,sq3,sq4,sq5,sq6,sq7,sq8)

        self.assertEqual(g.get_grid(),rand_grid)

class CheckGridTest(unittest.TestCase):
    pass

class CreateGridTest(unittest.TestCase):
    pass

class TestGetSquare(unittest.TestCase):
    pass


if __name__ == "__main__":
    unittest.main()
