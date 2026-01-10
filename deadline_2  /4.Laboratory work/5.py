print("Введите текст (для завершения нажмите Enter дважды):")

lines = []
while True:
    line = input()
    if line:
        lines.append(line)
    else:
        break

text = " ".join(lines)

if not text.strip():
    text = "Привет мир! Это тестовый текст. Привет еще раз."
    print(f"Текст не введен, использую демонстрационный:\n{text}")

import string

translator = str.maketrans('', '', string.punctuation)
clean_text = text.translate(translator).lower()

words = clean_text.split()

if not words:
    print("Текст не содержит слов!")
else:
    words_lower = [word.lower() for word in clean_text.split()]

    longest_word = max(words_lower, key=len)
    shortest_word = min(words_lower, key=len)

    avg_length = sum(len(word) for word in words_lower) / len(words_lower)

    from collections import Counter
    word_freq = Counter(words_lower)

    top_5_words = word_freq.most_common(5)

    print("РЕЗУЛЬТАТЫ АНАЛИЗА ТЕКСТА:")
    print(f"• Всего слов: {len(words_lower)}")
    print(f"• Уникальных слов: {len(word_freq)}")
    print(f"• Самое длинное слово: '{longest_word}' ({len(longest_word)} символов)")
    print(f"• Самое короткое слово: '{shortest_word}' ({len(shortest_word)} символов)")
    print(f"• Средняя длина слова: {avg_length:.1f} символов")
    
    print("ТОП-5 САМЫХ ЧАСТЫХ СЛОВ:")
    for i, (word, count) in enumerate(top_5_words, 1):
        percentage = (count / len(words_lower)) * 100
        print(f"{i}. '{word}': {count} раз ({percentage:.1f}%)")

    print("ДОПОЛНИТЕЛЬНАЯ СТАТИСТИКА:")
    print(f"• Все слова (первые 20): {words_lower[:20]}")

    print("РАСПРЕДЕЛЕНИЕ СЛОВ ПО ДЛИНЕ:")
    length_dist = {}
    for word in words_lower:
        length = len(word)
        length_dist[length] = length_dist.get(length, 0) + 1
    
    for length in sorted(length_dist.keys()):
        count = length_dist[length]
        bar = "|" * (count * 20 // len(words_lower))
        print(f"  {length} символов: {bar} {count} слов")