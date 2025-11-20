import string

text = input("Введите текст: ")

for char in string.punctuation:
    text = text.replace(char, '')

words = text.lower().split()

if not words:
    print("Текст не введен!")
    exit()

longest_word = max(words, key=len)
shortest_word = min(words, key=len)
average_length = sum(len(word) for word in words) / len(words)

word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1

top_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)[:5]

print(f"\nСамое длинное слово: {longest_word}")
print(f"Самое короткое слово: {shortest_word}")
print(f"Средняя длина: {average_length:.1f}")
print(f"Топ-5 слов: {top_words}")