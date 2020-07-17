class RingBuffer:
    def __init__(self, capacity):
        self.items = [None] * capacity
        self.capacity = capacity
        self.count = 0

    def append(self, item):
        self.items[self.count % self.capacity] = item
        self.count += 1

    def get(self):
        if self.count < self.capacity:
            return self.items[:self.count]
        else:
            return self.items