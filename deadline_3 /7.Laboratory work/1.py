from dataclasses import dataclass, field

@dataclass(frozen=True, repr=False)
class Product:
    name: str
    price: float = field(repr=False)
    weight: float
    is_available: bool = True
    
    def order_cost(self, quantity):
        return self.price * quantity
    
    def __repr__(self):
        return f"Product(name='{self.name}', weight={self.weight}, is_available={self.is_available})"


if __name__ == "__main__":
    apple = Product("Apple", 15.0, 0.2, True)
    print(apple)  # Product(name='Apple', weight=0.2, is_available=True)
    print(apple.order_cost(10))  # 150.0