def roman_to_arabic_simple(roman: str) -> int:
    roman = roman.strip().upper()
    
    values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100}
    
    symbols_values = []
    
    i = 0
    while i < len(roman):
        match roman[i]:
            case 'I':
                current = 1
            case 'V':
                current = 5
            case 'X':
                current = 10
            case 'L':
                current = 50
            case 'C':
                current = 100
            case _:
                return 0
        
        if i + 1 < len(roman):
            next_char = roman[i + 1]
            if next_char in values and current < values[next_char]:
                symbols_values.append(values[next_char] - current)
                i += 2
                continue
        
        symbols_values.append(current)
        i += 1
    

    return sum(symbols_values)


symbols_numbered = '10 11 25 1 3'
symbols = list(map(int, symbols_numbered.split()))
number = sum(symbols)

roman_input = input("Введите римскоен число: ")
result = roman_to_arabic_simple(roman_input)
print(f"Римское число '{roman_input}' = {result}")