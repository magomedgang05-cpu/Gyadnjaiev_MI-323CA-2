number = int(input("Введите положительное целое число: "))

total = 0
temp = number
digits = []

while temp > 0:
    digit = temp % 10
    digits.append(digit)
    total += digit
    temp //= 10

digits.reverse()

explanation = "+".join(map(str,digits))
print(f"{total} ({explanation})")