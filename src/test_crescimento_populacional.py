import unittest
import crescimento_populacional

class RoteiroTeste(unittest.TestCase):
    def test_ct01(self):
        res = crescimento_populacional.crescimento_populacional(99, 600, 5.0, 2.5)
        self.assertEqual (res, "Inválido")

    def test_ct02(self):
        res = crescimento_populacional.crescimento_populacional(100, 101, 5.0, 2.5)
        self.assertEqual (res, "1 anos")

    def test_ct03(self):
        res = crescimento_populacional.crescimento_populacional(1000000, 1000001, 5.0, 2.5)
        self.assertEqual (res, "Inválido")

    def test_ct04(self):
        res = crescimento_populacional.crescimento_populacional(1000001, 1000002, 5.0, 2.5)
        self.assertEqual (res, "Inválido")

    def test_ct05(self):
        res = crescimento_populacional.crescimento_populacional(500, 500, 5.0, 2.5)
        self.assertEqual (res, "Inválido")

    def test_ct06(self):
        res = crescimento_populacional.crescimento_populacional(500, 1000000, 5.0, 2.5)
        self.assertEqual (res, "Mais de um século")

    def test_ct07(self):
        res = crescimento_populacional.crescimento_populacional(500, 1000001, 5.0, 2.5)
        self.assertEqual (res, "Inválido")

    def test_ct08(self):
        res = crescimento_populacional.crescimento_populacional(500, 600, 0.0, -0.1)
        self.assertEqual (res, "Inválido")

    def test_ct09(self):
        res = crescimento_populacional.crescimento_populacional(500, 600, 0.1, 0.0)
        self.assertEqual (res, "Mais de um século")

    def test_ct10(self):
        res = crescimento_populacional.crescimento_populacional(500, 600, 10.0, 9.9)
        self.assertEqual (res, "Mais de um século")

    def test_ct11(self):
        res = crescimento_populacional.crescimento_populacional(500, 600, 10.1, 10.0)
        self.assertEqual (res, "Inválido")

    def test_ct12(self):
        res = crescimento_populacional.crescimento_populacional(500, 600, 5.0, -0.1)
        self.assertEqual (res, "Inválido")

    def test_ct13(self):
        res = crescimento_populacional.crescimento_populacional(500, 600, 9.0, 10.1)
        self.assertEqual (res, "Inválido")

    def test_ct14(self):
        res = crescimento_populacional.crescimento_populacional(500, 600, 5.0, 5.0)
        self.assertEqual (res, "Inválido")

if __name__ == "__main__":
    unittest.main()