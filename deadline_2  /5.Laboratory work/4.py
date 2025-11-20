import string

text = input("Введите текст: ")

translator = str.maketrans('', '', string.punctuation)
cleaned_text = text.translate(translator).lower()

words_set = set(cleaned_text.split())

print(f"\nУникальные слова: {len(words_set)}")
print(f"Все уникальные слова: {words_set}")

long_words = {word for word in words_set if len(word) > 5}
print(f"Длинные слова: {long_words}")

key_words = {'python', 'programming'}
found_key_words = key_words & words_set

print(f"Найдены ключевые слова: {bool(found_key_words)}")