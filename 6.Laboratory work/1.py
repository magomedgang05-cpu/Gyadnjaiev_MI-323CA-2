fio_input = input("Введите ваше ФИО через пробел: ")

fio_parts = fio_input.split()

formatted_parts = [part.capitalize() for part in fio_parts]

formatted_fio = ' '.join(formatted_parts)

print(f"Добро пожаловать, {formatted_fio}!")