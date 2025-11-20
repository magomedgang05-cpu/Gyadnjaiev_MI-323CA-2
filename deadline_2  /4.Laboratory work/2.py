numbers = [52, 42, 13, 14, 83, 88, 31, 76, 69, 18]

even_numbers = []
for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)

numbers_above_50 = []
for num in numbers:
    if num > 50:
        numbers_above_50.append(num)

print("Исходный список:", numbers)
print("Чётные числа:", even_numbers)
print("Числа больше 50:", numbers_above_50)