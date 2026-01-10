text = input("Введите произвольный текст: ")

word = input("Введите слово для поиска: ")

if word in text:
    count = text.count(word)
    print(f"Слово '{word}' найдено в тексте!")
    print(f"Количество встреч: {count}")
else:
    print(f"Слова '{word}' нет в тексте!")