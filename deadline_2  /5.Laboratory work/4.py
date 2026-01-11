text = input("Введите текст: ")

words = text.lower().split()
unique_words = set(words)

print(f"Уникальные слова: {len(unique_words)}")

long_words = {word for word in unique_words if len(word) > 5}
print(f"Длинные слова: {long_words}")

has_keywords = "python" in unique_words or "programming" in unique_words
print(f"Найдены ключевые слова: {has_keywords}")