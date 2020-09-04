from fractions import Fraction


# class Fraction:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def summa(self):
#         try:
#             return print(self.x + self.y)
#         except:
#             print('Ooops')

x = Fraction(1/2)
y = Fraction(1/4)
assert x + y == Fraction(3/4)