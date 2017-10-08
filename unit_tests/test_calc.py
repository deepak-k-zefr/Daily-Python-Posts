import unittest
import calc
class TestCalc(unittest.TestCase):

    def test_add(self):
        ''''Test Edge cases'''
        self.assertEquals(calc.add(10,5),15)
        self.assertEquals(calc.add(-3,-4),-7)
        self.assertEquals(calc.add(-4,5),1)

    def test_sub(self):
        ''''Test Edge cases'''
        self.assertEquals(calc.subtract(10,5),5)
        self.assertEquals(calc.subtract(-3,-4),1)
        self.assertEquals(calc.subtract(-4,5),-9)

    def test_mul(self):
        ''''Test Edge cases'''
        self.assertEquals(calc.multiply(10,5),50)
        self.assertEquals(calc.multiply(10,-5),-50)
        self.assertEquals(calc.multiply(2,3),6)

    def test_div(self):
        ''''Test Edge cases'''
        self.assertEquals(calc.divide(10,5),2)
        self.assertEquals(calc.divide(-3,-4),.75)
        self.assertEquals(calc.divide(-4,5),-0.8)

        ### Check assert
        self.assertRaises(ValueError,calc.divide,10,0)


if __name__ == '__main__':
    unitest.main()