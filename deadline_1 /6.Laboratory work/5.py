text = input("Введите произвольный текст:").strip()
search_word = input("Введите слово для поиска:").strip()

words = text.split()

count = 0
first_index = -1

for i, word in enumerate(words):
    if word.lower() == search_word.lower():
        count += 1
        if first_index == -1:
            first_index = i

text_without_word = text.replace(search_word, "")

print(f"Количество встреченных слов'{search_word}': {count}")
if first_index != -1:
    print(f"Индекс первого встреченного слова: {first_index}")
else:
    print("Слово не найдено")

print("Текст без указанного слова:")
print(text_without_word)