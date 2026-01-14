class DatabaseConfig:
    _instance = None
    
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._args = args
            cls._kwargs = kwargs
        return cls._instance
    
    def __init__(self, db_name=None, user=None, password=None):
        if not hasattr(self, '_initialized'):
            self.db_name = db_name
            self.user = user
            self.password = password
            self._initialized = True


if __name__ == "__main__":
    conf1 = DatabaseConfig("shop_db", "admin", "123")
    conf2 = DatabaseConfig("users_db", "root", "000")
    
    print(conf1 is conf2)
    print(conf2.db_name)
    
    print()
    
    print("Проверка атрибутов:")
    print(f"conf1.db_name: {conf1.db_name}")
    print(f"conf1.user: {conf1.user}")
    print(f"conf1.password: {conf1.password}")