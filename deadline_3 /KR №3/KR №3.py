class SingletonMeta(type):
    _instances = {}
    
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class HTMLReportMixin:
    def get_html(self):
        return f"<ul>{''.join(f'<li>{e}</li>' for e in self.events)}</ul>"


class EventLogger(HTMLReportMixin, metaclass=SingletonMeta):
    def __init__(self):
        self.events = []
    
    def add_event(self, text):
        self.events.append(text)


# Демонстрация работы
logger1 = EventLogger()
logger1.add_event("Запуск системы")

logger2 = EventLogger()
logger2.add_event("Ошибка подключения")

print(logger1.get_html())