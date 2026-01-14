class Vector3D:
    __slots__ = ('x', 'y', 'z')
    
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


if __name__ == "__main__":
    v = Vector3D(1, 2, 3)
    
    """Проверка __dict__"""
    print("Есть ли __dict__ у объекта?", hasattr(v, 'c'))
    
    """Проверка color"""
    try:
        v.color = "red"
    except AttributeError:
        print("Нельзя добавить новый атрибут 'color' - AttributeError")
    
    """Проверка всех атирбутов"""
    print(f"Существующие атрибуты работают: x={v.x}, y={v.y}, z={v.z}")