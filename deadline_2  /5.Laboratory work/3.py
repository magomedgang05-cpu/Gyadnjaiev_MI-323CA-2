colors = {
    "красный": (255, 0, 0),
    "зеленый": (0, 255, 0),
    "синий": (0, 0, 255),
    "желтый": (255, 255, 0),
    "голубой": (0, 255, 255),
    "белый": (255, 255, 255),
    "черный": (0, 0, 0)
}

print("Доступные цвета:")
for color_name, rgb in colors.items():
    print(f"- {color_name}: {rgb}")

print("\n" + "="*40)

def mix_colors(color1, color2):
    """Смешивает два цвета (среднее арифметическое)"""
    r1, g1, b1 = color1
    r2, g2, b2 = color2
    mixed = ((r1 + r2) // 2, (g1 + g2) // 2, (b1 + b2) // 2)
    return mixed

red = colors["красный"]
blue = colors["синий"]
purple = mix_colors(red, blue)
print(f"Смешиваем красный {red} и синий {blue}")
print(f"Получаем фиолетовый: {purple}")

print("\n" + "="*40)

def invert_color(color):
    """Инвертирует цвет (255 - значение)"""
    r, g, b = color
    inverted = (255 - r, 255 - g, 255 - b)
    return inverted

white = colors["белый"]
black = invert_color(white)
print(f"Инвертируем белый {white}")
print(f"Получаем черный: {black}")

red = colors["красный"]
cyan = invert_color(red)
print(f"Инвертируем красный {red}")
print(f"Получаем голубой: {cyan}")