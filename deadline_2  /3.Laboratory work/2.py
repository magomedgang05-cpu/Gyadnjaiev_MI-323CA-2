# Задание 2: Подсчёт символов в строке

# 1. Просим пользователя ввести строку
text = input("Введите произвольную строку: ")

# 2. Создаём пустой словарь для подсчёта
char_count = {}

# 3. Подсчитываем символы (без учёта регистра)
for char in text.lower():
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

# 4. Выводим полученный словарь
print(char_count)