def flat_gen(nested_list):
    for sublist in nested_list:
        yield from sublist


if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5],
        [6, 7, 8, 9]
    ]
    
    for num in flat_gen(matrix):
        print(num, end=" ")