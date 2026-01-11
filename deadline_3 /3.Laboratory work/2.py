def sum_digits(number):
    if abs(number) < 10:
        return abs(number)
    
    last_digit = abs(number) % 10
    remaining = abs(number) // 10
    
    return last_digit + sum_digits(remaining)


print(sum_digits(12345))