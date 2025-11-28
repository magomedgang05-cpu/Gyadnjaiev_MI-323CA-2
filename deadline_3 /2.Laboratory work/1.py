def squares_gen(n):
    for i in range(1, n + 1):
        yield i ** 2
gen =squares_gen(5)
for val in gen:
    print(val)