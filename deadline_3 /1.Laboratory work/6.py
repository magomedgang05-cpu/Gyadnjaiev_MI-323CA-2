def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(5)
def greet(name):
    print(f"Привет, {name}!")

greet("Мага")