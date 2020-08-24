# Task 3
#
# Create your own implementation of an iterable, which could be used inside for-in loop.
# Also, add logic for retrieving elements using square brackets syntax.

class Iterable:
    def __init__(self, iterator):
        self.iterator = iterator
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.iterator):
            res = self.iterator[self.index]
            self.index += 1
            return res
        raise StopIteration

    def __getitem__(self, item):
        if item <= len(self.iterator):
            return self.iterator[item-1]
        return False


my_list = Iterable(['A','B','C','D'])
print(my_list[2])
print('-'*10)
for i in my_list:
    print(i)
