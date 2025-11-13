text = input("Введите текст: ")

letters = 0
digits = 0
punctuation = 0
spaces = 0

punctuation_marks = ".,!?:;"

for char in text:
    if char.isalpha():
        letters += 1
    elif char.isdigit():
        digits += 1
    elif char in punctuation_marks:
        punctuation += 1
    elif char.isspace():
        spaces += 1

print("\nРезультат подсчёта:")
print("1. букв =", letters)
print("2. цифр =", digits)
print("3. знаков препинания =", punctuation)
print("4. пробелов =", spaces)