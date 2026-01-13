class SmartList(list):
    def __getitem__(self, index):
        if isinstance(index, int) and index < 0:
            positive_index = abs(index) - 1
            if positive_index < len(self):
                return super().__getitem__(positive_index)
            else:
                raise IndexError("list index out of range")
        else:
            return super().__getitem__(index)


if __name__ == "__main__":
    sl = SmartList([10, 20, 30])
    
    print(sl[0])
    print(sl[-1])
    print(sl[-2])