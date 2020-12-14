from square import Square as Square
import unittest
import random

class TestInit(unittest.TestCase):
    ''' tests the initialization of an empty square '''
    def test_init(self):
        ''' constructs a 0 matrix and compares it to a newly initialized square '''
        empty_square = [[0 for i in range(3)] for j in range(3)]
        x = Square()
        for i in range(3):
            self.assertEqual(empty_square[i],x.get_row(i))
            self.assertEqual([row[i] for row in empty_square],x.get_col(i))
        self.assertEqual(empty_square, x.get_square())

class TestAssignment(unittest.TestCase):
    ''' tests value assignment in square '''
    def test_val(self):
        ''' assigns random values to random positions and then checks '''
        val_tuple = (1,2,3,4,5,6,7,8,9)
        random_sq1 = [[random.choice(val_tuple) for i in range(3)] for j in range(3)]
        random_sq2 = [[random.choice(val_tuple) for i in range(3)] for j in range(3)]
        x = Square()
        y = Square()
        for i in range(3):
            for j in range(3):
                x.assign_val(i,j,random_sq1[i][j])
                y.assign_val(i,j,random_sq2[i][j])
        for i in range(3):
            self.assertEqual(x.get_row(i),random_sq1[i])
            self.assertEqual(y.get_row(i),random_sq2[i])
            self.assertEqual(x.get_col(i), [row[i] for row in random_sq1])
            self.assertEqual(y.get_col(i),[row[i] for row in random_sq2])
        self.assertEqual(x.get_square(),random_sq1)
        self.assertEqual(y.get_square(),random_sq2)

class TestSquareCheck(unittest.TestCase):
    ''' tests to see if the square checker finds an element '''
    def testSquarecChecker(self):
        test_vals = (random.randint(1,9),random.randint(1,9),random.randint(1,9))
        s = Square()
        for i in test_vals:
            self.assertEqual(False, s.check_num_square(i))
            for j in range(3):
                self.assertEqual(False, s.check_num_col(j,i))
                self.assertEqual(False,s.check_num_row(j,i))
        for i in range(3):
            for j in range(3):
                if i == j:
                    s.assign_val(i,j,test_vals[i])
                    self.assertEqual(True,s.check_num_row(i,test_vals[i]))
                    self.assertEqual(True, s.check_num_col(j,test_vals[i]))
        for i in test_vals:
            self.assertEqual(True, s.check_num_square(i))

if __name__ == "__main__":
    unittest.main()

        