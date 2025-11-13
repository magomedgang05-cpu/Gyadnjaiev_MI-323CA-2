# Задание 5: Статистика слов в тексте

print("Введите текст (пустая строка для завершения):")

text_lines = []
while True:
    line = input()
    if line.strip() == "":  # Проверяем пустую строку
        break
    text_lines.append(line)

# Проверяем, что есть введенный текст
if text_lines:
    # Объединяем все строки в один текст
    full_text = " ".join(text_lines)
    
    # Очищаем текст от знаков препинания и приводим к нижнему регистру
    import string
    translator = str.maketrans('', '', string.punctuation)
    cleaned_text = full_text.translate(translator).lower()
    
    # Разбиваем на слова
    words = cleaned_text.split()
    
    # Создаём словарь статистики
    word_stats = {}
    for word in words:
        if word in word_stats:
            word_stats[word] += 1
        else:
            word_stats[word] = 1
    
    print("\nСтатистика слов:", word_stats)
else:
    print("Текст не введен!")