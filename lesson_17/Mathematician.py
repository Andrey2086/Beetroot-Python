class Mathemat:

    def multiplication(self, a, b):
        return a * b

    def square_nums(self, nums):
        res = [i**2 for i in nums]
        return (res)

    def filter_leaps(self, year):
        leap_year = [i for i in year if i%4 == 0]
        return (leap_year)



