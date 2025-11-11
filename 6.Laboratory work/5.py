text = input("Введите произвольный текст: ")

search_word = input("Введите слово для поиска: ")

count = text.count(search_word)
first_index = text.find(search_word)

print(f"\nКоличество встреченных слов '{search_word}': {count}")

if first_index != -1:
    print(f"Индекс первого встреченного слова: {first_index}")
else:
    print("Слово не найдено в тексте")

text_without_word = text.replace(search_word, "")
print(f"\nТекст без слова '{search_word}':")
print(text_without_word)