class EvenNumbers:

    def __init__(self, start, end):
        if start % 2 != 0:
            start += 1
        self.start = start
        self.end = end

    def __iter__(self):
        self.i = 0
        return self

    def __next__(self):
        self.i += 1
        if self.i > 1:
            if self.start >= self.end-1:
                raise StopIteration()
            self.start += 2
        return self.start

en = EvenNumbers(10, 25)
print (en)
for value in en:
    print (value)
