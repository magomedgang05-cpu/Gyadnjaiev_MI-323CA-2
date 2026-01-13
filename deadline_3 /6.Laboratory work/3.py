class Multiplier:
    def __init__(self, multiplier):
        self.multiplier = multiplier
    
    def __call__(self, number):
        return self.multiplier * number


if __name__ == "__main__":
    by_5 = Multiplier(5)
    print(by_5(10))  # 50
    print(by_5(2))   # 10