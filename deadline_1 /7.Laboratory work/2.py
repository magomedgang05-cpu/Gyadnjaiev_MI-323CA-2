print("=== РЕГИСТРАЦИЯ ===")
password = input("Придумайте пароль: ")
confirm_password = input("Подтвердите пароль: ")

if password == confirm_password:
    print("Пароль успешно установлен!")
else:
    print("Пароли не совпадают! Попробуйте снова.")
    exit()

print("\n" + "="*30)

print("=== АВТОРИЗАЦИЯ ===")
login_password = input("Введите пароль для входа: ")

if login_password == password:
    print("Access")
else:
    print("Denied")