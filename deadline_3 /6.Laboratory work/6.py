class Frange:
    def __init__(self, start, stop=None, step=None):
        if stop is None:
            self.start = 0.0
            self.stop = float(start)
            self.step = 1.0
        elif step is None:
            self.start = float(start)
            self.stop = float(stop)
            self.step = 1.0
        else:
            self.start = float(start)
            self.stop = float(stop)
            self.step = float(step)
        
        self.current = self.start
    
    def __iter__(self):
        self.current = self.start
        return self
    
    def __next__(self):
        if self.step > 0 and self.current >= self.stop:
            raise StopIteration
        elif self.step < 0 and self.current <= self.stop:
            raise StopIteration
        
        value = self.current
        self.current += self.step
        return value


if __name__ == "__main__":
    for x in Frange(1, 3, 0.5):
        print(x)