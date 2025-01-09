from funcs import *
import unittest


class TestMaxListes(unittest.TestCase):
    def test_max_listes(self):
        self.assertEqual(max_listes([1, 2, 3, 4, 5, 6]), [4, 5, 6])
        self.assertEqual(max_listes([6, 5, 4, 3, 2, 1]), [4, 5, 6])
        self.assertEqual(max_listes([462, 427, 404, 332, 838]), [427, 462, 838])
        self.assertEqual(max_listes([128, 854, 102, 710, 44]), [128, 710, 854])
        self.assertEqual(max_listes([301, 250, 552, 384, 474]), [384, 474, 552])

if __name__ == '__main__':
    unittest.main()
