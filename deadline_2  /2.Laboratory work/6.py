def draw_spiral(n):
    if n <= 0:
        print("число должно быть положительным")
        return

    if n % 2 == 0:
        n += 1

    spiral = [[0] * n for _ in range(n)]
    
    x = y = n // 2
    spiral[x][y] = 1
    
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # вправо, вниз, влево, вверх
    dir_idx = 0
    
    step = 1
    steps_done = 0
    turns = 0
    
    for num in range(2, n * n + 1):
        dx, dy = directions[dir_idx]
        x += dx
        y += dy
        spiral[x][y] = num
        
        steps_done += 1
        
        if steps_done == step:
            steps_done = 0
            dir_idx = (dir_idx + 1) % 4
            turns += 1
            
            if turns == 2:
                step += 1
                turns = 0
    
    max_width = len(str(n * n))
    
    for row in spiral:
        print(" ".join(f"{num:>{max_width}}" for num in row))


if __name__ == "__main__":
    try:
        n = int(input("Ведите число n:"))
        draw_spiral(n)
    except:
        print("Ошибка ввода!")