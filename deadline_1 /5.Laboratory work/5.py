import random
import string

def generate_random_letters(length: int) -> str:
    """"Генерирует случайную строку только из букв."""
    return ''.join(random.choice(string.ascii_letters) for i in range(length))

message = input("Введите сообщение для кодирования: ")
n = int(input("Введите количество подставляемых символов (n): "))

encoded_massege = ""
for char in message:
    encoded_massege += char + generate_random_letters(n)

print("\n Закодированное сообщение")
print(encoded_massege)