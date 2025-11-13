text = input("Введите строчку: ")

vowels = "аеёиоуыэюяaeiouyAEIOUYАЕЁИОУЫЭЮЯ"
results =[]
i = 0
while i < len(text):
    if text[i] not in vowels:
        results.append(text[i])
    i += 1

results_text = ''.join(results)
print(results_text)