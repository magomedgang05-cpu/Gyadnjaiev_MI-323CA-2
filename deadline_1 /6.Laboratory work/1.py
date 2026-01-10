fio_input = input("Введите ФИО через пробел: ").strip()

fio_parts = fio_input.split()

formatted_parts = []
for part in fio_parts:
    if part:
        formatted_parts.append(part[0].upper() + part[1:].lower())

formatted_fio = " ".join(formatted_parts)

print(f"Добро пожаловать {formatted_fio}")