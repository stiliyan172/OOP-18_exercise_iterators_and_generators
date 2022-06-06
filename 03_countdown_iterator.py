class countdown_iterator:
    def __init__(self, count: int):
        self.count = count
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.i <= self.count:
            count_el = self.count
            self.count -= 1
            return count_el
        else:
            raise StopIteration


iterator = countdown_iterator(10)
for item in iterator:
    print(item, end=" ")
