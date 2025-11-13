text = input("Введите строчку:")

cleaned_text = text.replace(" ","").lower()

is_palindrome = True
left = 0
right = len(cleaned_text) - 1

while left < right:
    if cleaned_text[left] != cleaned_text[right]:
        is_palindrome = False
        break
    left += 1
    right -= 1

if is_palindrome:
    print("Да, это палиндром")
else:
    print("Нет, это не палиндром")