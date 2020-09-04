import unittest
# from homework10.phonebook import Car, Engine, EngieBenzin, EngineDiesel
from main_svyat import MyIter
# stih1 = '''1111
# 2222
# 333
# 444'''
#
# stih2 = '''qqqq
# wwww
# ee'''
#
# def mix_stih(*args):
#     yield 'qwert'
#

class MyTest(unittest.TestCase):

    def test_iterator_09(self):
        for i in MyIter(1,10,1):
            return i
        self.assertEqual(i, 9)

    def test_iterator_90(self):
        for i in MyIter(10,0, 1):
            return i
        self.assertEqual(i, 1)

    def test_indexiter(self):
        gen = MyIter(0,20, 4)
        self.assertEqual(gen[0], 0)
        self.assertEqual(gen[1], 4)
        self.assertEqual(gen[2], 8)
        with self.assertRaises(IndexError):
            print(gen [-5])
        with self.assertRaises(IndexError):
            print(gen [50])

#
# if __name__ == '__main__':
#     unittest.main_svyat()