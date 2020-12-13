import unittest
import random

class TestInit(unittest.TestCase):
    ''' tests the initialization of an empty square '''
    def test_init(self):
        ''' constructs a 0 matrix and compares it to a newly initialized square '''
        empty_square = [[0 for i in range(3)] for j in range(3)]
        x = Square()
        x.print_square
        for i in range(3):
            self.assertEqual(empty_square[i],x.get_row(i))
            self.assertEqual(empty_square[:,i],x.get_col(i))
        self.assertEqual(empty_square, x.get_square)
        for i in range(3):
            print(x.get_row(i))

class TestAssignment(unittest.TestCase):
    ''' tests value assignment in square '''
    def test_val(self):
        ''' assigns random values to random positions and then checks '''
        val_tuple = (1,2,3,4,5,6,7,8,9)
        random_sq1 = [[random.choice(val_tuple) for i in range(3)] for j in range(3)]
        random_sq2 = [[random.choice(val_tuple) for i in range(3)] for j in range(3)]
        print("Random Square 1:")
        for row in random_sq1:
            print(row)
        print("Random Square 2:")
        for row in random_sq2:
            print(row)
        x = Square()
        y = Square()
        for i in range(3):
            for j in range(3):
                x.assign_val(i,j,random_sq1[i][j])
                y.assign_val(i,j,random_sq2[i][j])
        for i in range(3):
            self.assertEqual(x.get_row(i),random_sq1[i])
            self.assertEqual(y.get_row(i),random_sq2[i])
        self.assertEqual(x.get_square,random_sq1)
        self.assertEqual(y.get_square,random_sq2)

if __name__ == "__main__":
    unittest.main()

        