import unittest;
from placar import Placar;

class TestPlacar(unittest.TestCase):

    def setUp(self):
        self.p = Placar()

    def test_checkSeqMaiorTrue(self):
        self.assertTrue(self.p.checkSeqMaior([1,2,3,4,5]))

    def test_checkSeqMaiorQ4(self):
        v = [1,2,3,4,4]  
        self.assertFalse(self.p.checkSeqMaior(v))

    def test_checkSeqMaiorQ3(self):
        v = [1,2,3,3,4]  
        self.assertFalse(self.p.checkSeqMaior(v))

    def test_checkSeqMaiorQ2(self):
        v = [1,2,2,3,4] 
        self.assertFalse(self.p.checkSeqMaior(v))

    def test_checkSeqMaiorQ1(self):
        v = [1,1,2,3,4] 
        self.assertFalse(self.p.checkSeqMaior(v))

    def test_checkQuinaTrue(self):
        v=[4,4,4,4,4]
        self.assertTrue(self.p.checkQuina(v))

    def test_checkQuinaQ5(self):
        v = [5,5,5,5,6]  
        self.assertFalse(self.p.checkQuina(v))

    def test_checkQuinaQ4(self):
        v = [5,5,5,6,6]  
        self.assertFalse(self.p.checkQuina(v))

    def test_checkQuinaQ3(self):
        v = [5,5,6,6,6] 
        self.assertFalse(self.p.checkQuina(v))

    def test_checkQuinaQ2(self):
        v = [6,5,6,6,6] 
        self.assertFalse(self.p.checkQuina(v))

    def test_checkQuinaQ1(self):
        v = [5,6,6,6,6] 
        self.assertFalse(self.p.checkQuina(v))

    def test_checkFull3(self):
        v=[1,1,1,3,3]
        self.assertTrue(self.p.checkFull(v))

    def test_checkFullFalse(self):
        v = [1,2,3,4,5]
        self.assertFalse(self.p.checkFull(v))

    def test_checkQuadraFF(self):
        v = [1,2,3,4,5]
        self.assertFalse(self.p.checkQuadra(v))

    def test_checkQuadraQ5(self):
        self.p.add(9, [4,4,4,4,5])
        self.assertEqual(self.p.getScore(), 30)

    def test_checkQuadraQ3(self):
        self.assertFalse(self.p.checkQuadra([2,2,2,3,4]))

    def test_checkFull5(self):
        v = [3, 3, 4, 3, 3]
        self.assertFalse(self.p.checkFull(v))
