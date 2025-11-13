numbers = input("Введите числа через запятуюю:").split(',')

count = 0
i = 0

while i < len(numbers):
    num = int(numbers[i].strip())
    if num == 0:
        break
    count += 1
    i += 1

print(count)