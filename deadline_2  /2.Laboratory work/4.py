n = int(input("Введите высоту пирамиды: "))

for i in range(1, n + 1):
    left_part = ''.join(str(x) for x in range(1, i + 1))
    right_part = ''.join(str(x) for x in range(i - 1, 0, -1))
    pyramid_line = left_part + right_part
    
    spaces = ' ' * (n - i)
    print(spaces + pyramid_line)