colors = {
    "красный": (255, 0, 0),
    "зеленый": (0, 255, 0),
    "синий": (0, 0, 255),
    "желтый": (255, 255, 0),
    "фиолетовый": (128, 0, 128),
    "бирюзовый": (64, 224, 208),
    "оранжевый": (255, 165, 0)
}

color1 = "красный"
color2 = "синий"
rgb1 = colors[color1]
rgb2 = colors[color2]

mixed_rgb = tuple((rgb1[i] + rgb2[i]) // 2 for i in range(3))

color_names = {
    (255, 0, 0): "красный",
    (0, 255, 0): "зеленый",
    (0, 0, 255): "синий",
    (255, 255, 0): "желтый",
    (128, 0, 128): "фиолетовый",
    (64, 224, 208): "бирюзовый",
    (255, 165, 0): "оранжевый",
    (127, 0, 127): "пурпурный",
    (0, 255, 255): "голубой"
}

result_color = color_names.get(mixed_rgb, f"неизвестный цвет {mixed_rgb}")
print(f"Смешивание цветов ({color1} + {color2}): {result_color} ({mixed_rgb})")

invert_color = "красный"
invert_rgb = colors[invert_color]
inverted_rgb = tuple(255 - invert_rgb[i] for i in range(3))

inverted_color_name = color_names.get(inverted_rgb, f"неизвестный цвет {inverted_rgb}")
print(f"Инвертированный цвет - {invert_color}: {inverted_color_name} ({inverted_rgb})")