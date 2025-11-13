from random import randint
random_num = randint(1, 100)
attempts = 0

print("Угадайте число от 1 до 100")

while True:
    guess = int(input("Ваша попытка:"))
    attempts += 1

    if guess == random_num:
        print("Ты угадал!")
        break
    elif guess > random_num:
        print("Меньше")
    else:
        print("Больше")

print(f"Число было: {random_num}")
print(f"Количество попыток: {attempts}")