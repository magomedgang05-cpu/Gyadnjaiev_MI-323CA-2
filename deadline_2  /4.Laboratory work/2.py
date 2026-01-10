import random
numbers = [random.randint(1, 100) for _ in range(10)]
print(f"Исходный список: {numbers}")

even_numbers = [num for num in numbers if num % 2 == 0]

numbers_above_50 = [num for num in numbers if num > 50]

print(f"1. Исходный список (10 чисел): {numbers}")
print(f"2. Четные числа: {even_numbers}")
print(f"3. Числа больше 50: {numbers_above_50}")

print("\nСтатистика фильтрации:")
print(f"   Всего чисел: {len(numbers)}")
print(f"   Четных чисел: {len(even_numbers)}")
print(f"   Чисел > 50: {len(numbers_above_50)}")
