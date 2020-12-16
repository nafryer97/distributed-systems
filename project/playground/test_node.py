from node import Node as Node
import unittest
import random

class TestInit(unittest.TestCase):
    ''' tests the initialization of 9 nodes '''
    def test_init(self):
        empty_node = [[0 for i in range(3)] for j in range(3)]
        for i in range(9):
            n = Node(i)
            self.assertEqual(i,n.get_position())
            self.assertEqual(empty_node,n.get_square())

if __name__ == "__main__":
    unittest.main()