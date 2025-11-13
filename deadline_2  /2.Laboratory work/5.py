count = int(input("Сколько чисел вы хотите ввести? "))

numbers = []
total = 0

for i in range(count):
    num = float(input(f"Введите число {i + 1}: "))
    numbers.append(num)
    total += num

max_num = numbers[0]
min_num = numbers[0]
average = total / count

for num in numbers:
    if num > max_num:
        max_num = num
    if num < min_num:
        min_num = num

above_average = 0
for num in numbers:
    if num > average:
        above_average += 1

print("\n Результаты:")
print(f"Максимальное: {max_num}")
print(f"Минимальное: {min_num}")
print(f"Среднее: {average}")
print(f"Чисел больше среднего: {above_average}")