from funcs import *
import unittest


class TestMaxListes(unittest.TestCase):
    def test_max_listes(self):
        self.assertEqual(max_listes([1, 2, 3, 4, 5, 6]), [4, 5, 6])
        self.assertEqual(max_listes([6, 5, 4, 3, 2, 1]), [4, 5, 6])
        self.assertEqual(max_listes([462, 427, 404, 332, 838]), [427, 462, 838])
        self.assertEqual(max_listes([128, 854, 102, 710, 44]), [128, 710, 854])
        self.assertEqual(max_listes([301, 250, 552, 384, 474]), [384, 474, 552])


class TestNombrePremier(unittest.TestCase):
    def test_nombres_premiers(self):
        self.assertEqual(1, False)
        self.assertEqual(2, True)
        self.assertEqual(3, True)
        self.assertEqual(7, True)
        self.assertEqual(17, True)
        self.assertEqual(4, False)
        self.assertEqual(9, False)
        self.assertEqual(15, False)
        self.assertEqual(0, False)
        self.assertEqual(-7, False)


if __name__ == '__main__':
    unittest.main()
