from typing import List, Any

def build_query(table_name: str, columns: List[str], **kwargs: Any) -> str:
    """
    Генерирует SQL-запрос SELECT для указанной таблицы с фильтрацией.
    
    Аргументы:
        table_name: Название таблицы в базе данных.
        columns: Список названий столбцов для выборки.
        **kwargs: Условия фильтрации в формате ключ=значение для секции WHERE.
    
    Возвращает:
        SQL-запрос в виде строки.
    """
    columns_part = ", ".join(columns)
    
    conditions = []
    for column_name, filter_value in kwargs.items():
        if isinstance(filter_value, str):
            conditions.append(f"{column_name}='{filter_value}'")
        else:
            conditions.append(f"{column_name}={filter_value}")
    
    if conditions:
        where_clause = " AND ".join(conditions)
        return f"SELECT {columns_part} FROM {table_name} WHERE {where_clause};"
    else:
        return f"SELECT {columns_part} FROM {table_name};"

print(build_query("users", ["name", "email"], age=25, city="Moscow", status="active"))