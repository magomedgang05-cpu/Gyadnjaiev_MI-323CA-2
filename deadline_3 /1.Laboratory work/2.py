def make_bold(func):
    def wrapper():
        result = func()
        return f"<b>{result}</b>"
    return wrapper

@make_bold
def get_text():
    return "Hello, World!"

print(get_text())