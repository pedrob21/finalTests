import unittest;
from placar import Placar;

class TestPlacar(unittest.TestCase):

    def setUp(self):
        self.p = Placar()

    def test_add(self):
        self.p.add(3, [3, 3, 3, 2, 2])

        placar = str(self.p)

        esperado = (
                "(1)    |   (7)    |  (4) \n"
                "-------|----------|-------\n"
                "(2)    |   (8)    |  (5) \n"
                "-------|----------|-------\n"
                " 9     |   (9)    |  (6) \n"
                "-------|----------|-------\n"
                "       |   (10)   |\n"
                "       +----------+\n"
            )
        self.assertEqual(placar, esperado)

    def test_umalinha(self):
        self.assertEqual(self.p.uma_linha(2), "(3) ")

    def test_getScore(self):
        self.p.add(6, [4, 6, 2, 6, 6])
        self.assertEqual(self.p.getScore(5), 18)

    def test_getTaken(self):
        self.assertFalse(self.p.getTaken(1))

    def test_getName(self):
        self.assertEqual(self.p.getName(0), "Ones")

    def test_conta(self):
        self.assertEqual(self.p.conta(6, [6,6,3,4,5]), 2)

    def test_checkFull(self):
        self.p.add(7, [2,5,2,2,5])
        self.assertEqual(self.p.getScore(), 15)

    def test_checkSeqMaior(self):
        self.p.add(8, [6,6,3,4,5])
        self.assertEqual(self.p.getScore(), 0)

    def test_checkQuadra(self):
        self.p.add(9, [4,4,4,4,1])
        self.assertEqual(self.p.getScore(), 30)

    def test_checkQuina(self):
        self.p.add(10, [5,5,5,5,5])
        self.assertEqual(self.p.getScore(), 40)

    def test_addInvalida(self):
        with self.assertRaises(IndexError):
            self.p.add(11, [1,2,3,4,5])

    def test_addOcupada(self):
        self.p.add(1, [1,1,1,2,3])
        with self.assertRaises(ValueError):
            self.p.add(1, [1,2,3,4,5])

    def test_addZero(self):
        with self.assertRaises(IndexError):
            self.p.add(0, [1,2,3,4,5])

    def test_add_posicao_valida(self):
        self.p.add(5, [2,3,3,4,1])
        self.assertTrue(self.p.getTaken(4))

    def test_checkFull2(self):
        self.p.add(7, [3,3,2,2,2])
        self.assertEqual(self.p.getScore(), 15)

    def test_checkFullFalse(self):
        self.assertFalse(self.p.checkFull([1,1,1,4,5]))

    def test_checkSeqMaiorTrue(self):
        self.assertTrue(self.p.checkSeqMaior([1,2,3,4,5]))

