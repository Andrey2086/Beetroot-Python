#        Task 2
#
# Create your own implementation of a built-in function range, named in_range(),
# which takes three parameters: `start`, `end`, and optional step. Tips: See the documentation for `range` function

def in_range(start, end, step=1):
    while start <= end:
        yield start
        start += step

for i in in_range(1, 5):
    print(i)
print('-'*10)
for i in in_range(0, 21, 5):
    print(i)

