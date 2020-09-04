class MyIter:
    def __init__(self, start, stop, step=1):
        self.start = start
        self.stop = stop
        self.step = abs(step)
        self.direction = True if start<stop else False

    @property
    def is_ok(self):
        return (self.start < self.stop) if self.direction else (self.start > self.stop)

    def __iter__(self):
        return self

    def __next__(self):
        if self.is_ok:
            ret = self.start
            self.start += self.step  if self.direction else -1*self.step
            return ret

        else:
            raise StopIteration

    def __getitem__(self, item):
        if item < 0:
            raise IndexError
        if self.stop < self.step*item:
            raise IndexError
        return self.step*item
