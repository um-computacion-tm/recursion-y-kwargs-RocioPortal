import unittest

def factorial(n):
    if n==1:               #caso base
        return 1
    resultado = n * factorial(n-1)   
    return resultado
    


class TestFactorial(unittest.TestCase):
    def test_con_1(self):
        resultado= factorial(1)
        self.assertEqual(resultado, 1)

    def test_con_2(self):
        resultado= factorial (2)
        self.assertEqual(resultado, 2)

    def test_con_3(self):
        resultado= factorial(3)
        self.assertEqual(resultado, 6)

    def test_con_4(self):
        resultado= factorial(4)
        self.assertEqual(resultado, 24)

    def test_con_5(self):
        resultado= factorial(5)
        self.assertEqual(resultado, 120)

    def test_con_6(self):
        resultado= factorial(6)
        self.assertEqual(resultado, 720)

    def test_con_7(self):
        resultado= factorial(7)
        self.assertEqual(resultado, 5040)
    
    def test_con_8(self):
        resultado= factorial(8)
        self.assertEqual(resultado, 40320)




unittest.main()