symbol = input("Введите символ для рисования:")
height = int(input("Введите высоту прямоугольника"))
width = int(input("Введите ширину прямоугольика"))

print()

row = 0
while row < height:
    col = 0
    while col < width:
        print(symbol, end='')
        col += 1
    print()
    row += 1