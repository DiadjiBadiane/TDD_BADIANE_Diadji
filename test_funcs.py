from funcs import *
import unittest


#Tests de l' exercice 1
class TestMaxListes(unittest.TestCase):
    def test_max_listes(self):
        self.assertEqual(max_listes([1, 2, 3, 4, 5, 6]), [4, 5, 6])
        self.assertEqual(max_listes([6, 5, 4, 3, 2, 1]), [4, 5, 6])
        self.assertEqual(max_listes([462, 427, 404, 332, 838]), [427, 462, 838])
        self.assertEqual(max_listes([128, 854, 102, 710, 44]), [128, 710, 854])
        self.assertEqual(max_listes([301, 250, 552, 384, 474]), [384, 474, 552])


class TestNombrePremier(unittest.TestCase):
    def test_nombres_premiers(self):
        self.assertEqual(nombre_premier(1), False)
        self.assertEqual(nombre_premier(2), True)
        self.assertEqual(nombre_premier(3), True)
        self.assertEqual(nombre_premier(7), True)
        self.assertEqual(nombre_premier(17), True)
        self.assertEqual(nombre_premier(4), False)
        self.assertEqual(nombre_premier(9), False)
        self.assertEqual(nombre_premier(15), False)
        self.assertEqual(nombre_premier(0), False)
        self.assertEqual(nombre_premier(-7), False)

class TestEstArithmetique(unittest.TestCase):
    def test_est_arithmetique(self):
        self.assertEqual(est_arithmetique([2, 4, 6, 8, 10]), True)
        self.assertEqual(est_arithmetique([10, 7, 4, 1, -2]), True)
        self.assertEqual(est_arithmetique([1, 1, 1, 1]), True)
        self.assertEqual(est_arithmetique([1, 3, 6, 10]), False)
        self.assertEqual(est_arithmetique([1]), True)
        self.assertEqual(est_arithmetique([1, 2]), True)
        self.assertEqual(est_arithmetique([]), True)
        self.assertEqual(est_arithmetique([5, 8, 11, 15]), False)



#Tests de l' exercice 2
class TESTFIFO(unittest.TestCase):
    def setUp(self):
        self.fifo = FIFO()

    def test_est_vide_fifo(self):
        self.assertTrue(self.fifo.est_vide())
        self.assertEqual(self.fifo.taille(), 0)

    def test_enfiler_defiler(self):
        self.fifo.enfiler(1)
        self.fifo.enfiler(2)
        self.fifo.enfiler(3)
        self.assertEqual(self.fifo.taille(), 3)
        self.assertEqual(self.fifo.defiler(), 1)
        self.assertEqual(self.fifo.defiler(), 2)
        self.assertEqual(self.fifo.taille(), 1)

class  TESTLIFO(unittest.TestCase):
    def setUp(self):
        self.lifo = LIFO()

    def test_est_vide_lifxo(self):
        self.assertTrue(self.lifo.est_vide())
        self.assertEqual(self.lifo.taille(), 0)

    def test_emplier_depiler(self):
        self.lifo.empiler(1)
        self.lifo.empiler(2)
        self.lifo.empiler(3)
        self.assertEqual(self.lifo.taille(), 3)
        self.assertFalse(self.lifo.est_vide())
        
        self.assertEqual(self.lifo.depiler(), 3)
        self.assertEqual(self.lifo.depiler(), 2)
        self.assertEqual(self.lifo.depiler(), 1)
        self.assertTrue(self.lifo.est_vide())





if __name__ == '__main__':
    unittest.main()
