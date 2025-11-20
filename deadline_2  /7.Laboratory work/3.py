def calc_avg(numbers: list[float]) -> float:
    """
    Вычисляет среднее арифметическое значение списка чисел.
    
    Args:
        numbers (list[float]): Список чисел для вычисления среднего
        
    Returns:
        float: Среднее арифметическое значение. Возвращает 0.0 для пустого списка
    """
    if not numbers:
        return 0.0
    return sum(numbers) / len(numbers)


def fmt_fio(parts: list[str], capitalize: bool = True) -> str:
    """
    Форматирует ФИО из списка частей имени.
    
    Args:
        parts (list[str]): Список частей имени (фамилия, имя, отчество)
        capitalize (bool, optional): Приводить ли первую букву каждого слова к верхнему регистру. 
                                   По умолчанию True.
        
    Returns:
        str: Отформатированная строка с ФИО
    """
    fio = " ".join(parts)

    if capitalize:
        return fio.title()

    return fio


def filter_scores(data_dict: dict[str, int], min_value: int) -> dict[str, int]:
    """
    Фильтрует словарь с оценками, оставляя только те, которые не ниже минимального значения.
    
    Args:
        data_dict (dict[str, int]): Словарь с предметами и оценками
        min_value (int): Минимальное значение оценки для включения в результат
        
    Returns:
        dict[str, int]: Отфильтрованный словарь с оценками, не ниже min_value
    """
    result = {}

    for key, value in data_dict.items():
        if value >= min_value:
            result[key] = value

    return result


# Примеры использования всех функций
if __name__ == "__main__":
    print("=== Функция 1: calc_avg ===")
    numbers_list = [10, 20, 30, 40]
    average = calc_avg(numbers_list)
    print(f"Среднее значение {numbers_list}: {average}")
    print(f"Среднее пустого списка: {calc_avg([])}")
    
    print("\n=== Функция 2: fmt_fio ===")
    fio1 = fmt_fio(['петров', "иван", "сергеевич"])
    print(f"ФИО с capitalize=True: {fio1}")
    
    fio2 = fmt_fio(['сидорова', "анна", "валерьевна"], capitalize=False)
    print(f"ФИО с capitalize=False: {fio2}")
    
    print("\n=== Функция 3: filter_scores ===")
    scores = {"math": 95, "history": 78, "english": 88, "art": 92}
    filtered = filter_scores(scores, 90)
    print(f"Исходные оценки: {scores}")
    print(f"Оценки >= 90: {filtered}")