import math

expression = input("Введите выражение (число1 знак число2): ")
parts = expression.split()

if len(parts) == 3:
    try:
        num1 = float(parts[0])
        operator = parts[1]
        num2 = float(parts[2])
        
        result = None
        
        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 != 0:
                result = num1 / num2
            else:
                print("Ошибка: деление на ноль!")
        elif operator == '%':
            result = num1 % num2
        elif operator == '//':
            if num2 != 0:
                result = num1 // num2
            else:
                print("Ошибка: деление на ноль!")
        elif operator == '**':
            result = num1 ** num2
        elif operator == '%%':
            result = (num2 / 100) * num1
        elif operator == '/**':
            if num1 >= 0:
                result = math.sqrt(num1)
            else:
                print("Ошибка: нельзя извлечь корень из отрицательного числа!")
        else:
            print("Ошибка: неизвестный оператор!")
        
        if result is not None:
            print(f"Результат: {result}")
            
    except ValueError:
        print("Ошибка: введите числа корректно!")
else:
    print("Ошибка: введите выражение в формате 'число1 знак число2'")