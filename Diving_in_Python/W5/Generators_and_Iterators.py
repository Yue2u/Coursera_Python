# Iterators
import pdb


class MyRangeIterator:
    def __init__(self, top):
        self.top = top
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.top:
            raise StopIteration

        current = self.current
        self.current += 1
        return current


# counter = MyRangeIterator(3)
# for i in counter:
#     print(i)


def MyRangeGenerator(top):
    current = 0
    while current < top:
        yield current
        current += 1


counter = MyRangeGenerator(3)
for i in counter:
    print(i)
