import unittest
from Mathematician import Mathemat

class My_test(unittest.TestCase):

    def test_multiplication(self):
        num = Mathemat().multiplication(2, 4)
        self.assertEqual(num, 8)

    def test_square_nums(self):
        list_1 = Mathemat().square_nums([-2, 3])
        self.assertEqual(list_1, [4, 9])

    def test_filter_leaps(self):
        list_2 = Mathemat().filter_leaps([1883, 2020])
        self.assertEqual(list_2, [2020])


if __name__ == '__main__':
    unittest.main()
