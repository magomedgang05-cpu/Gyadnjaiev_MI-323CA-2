import time

class Timer:
    def __enter__(self):
        self.start_time = time.time()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end_time = time.time()
        self.duration = self.end_time - self.start_time
        print(f"Время выполнения: {self.duration:.2f} сек")
        # Возвращаем False, чтобы не подавлять исключения
        return False


if __name__ == "__main__":
    with Timer():
        time.sleep(1.5)