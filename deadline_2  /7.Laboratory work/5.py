def format_report(report_title: str, *data: str, **properties: str) -> None:
    print(f"-- Отчет: {report_title} --")
    
    print("Данные:")
    if data:
        for item in data:
            print(f"  - {item}")
    else:
        print("  - Нет данных")
    
    print("Свойства:")
    if properties:
        for key, value in properties.items():
            print(f"  - {key}: {value}")
    else:
        print("  - Нет свойств")
    print()

format_report(
    "божественный отчет",
    "Продажи выросли на 101%",
    "Новых клиентов: 42",
    author="Гянджалиев И.В.",
    date="2001-09-12"
)