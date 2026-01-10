from random import randint, choice

class SimpleFruitStand:
    def __init__(self, name):
        self.name = name
        self.day = 1
        self.money = 1000
        
        self.counter = {
            'Яблоки': {'max': 50, 'current': 30},
            'Бананы': {'max': 40, 'current': 20},
            'Апельсины': {'max': 30, 'current': 15}
        }
        
        self.store = {
            'Яблоки': {'max': 200, 'current': 100},
            'Бананы': {'max': 150, 'current': 80},
            'Апельсины': {'max': 100, 'current': 50}
        }
        
        self.price = {
            'Яблоки': {'sale_price': 15, 'purchase_price': 8},
            'Бананы': {'sale_price': 20, 'purchase_price': 12},
            'Апельсины': {'sale_price': 25, 'purchase_price': 15}
        }
        
        print(f"Ларек '{name}' открыт!")
        print(f"Деньги: {self.money}, Цель: 10 дней")
    
    def show_status(self):
        print(f"\n--- День {self.day} ---")
        print(f"Деньги: {self.money}")
        
        print("\nПрилавок:")
        for fruit, data in self.counter.items():
            print(f"  {fruit}: {data['current']}/{data['max']}")
        
        print("\nЗапас:")
        for fruit, data in self.store.items():
            print(f"  {fruit}: {data['current']}/{data['max']}")
    
    def redistribute(self):
        for fruit in self.counter:
            need = self.counter[fruit]['max'] - self.counter[fruit]['current']
            have = self.store[fruit]['current']
            move = min(need, have)
            
            if move > 0:
                self.counter[fruit]['current'] += move
                self.store[fruit]['current'] -= move
                print(f"Перемещено {move} {fruit}")
    
    def buy_fruits(self):
        print("\nПокупка фруктов:")
        fruits = list(self.store.keys())
        
        for i, fruit in enumerate(fruits, 1):
            price = self.price[fruit]['purchase_price']
            print(f"{i}. {fruit} - {price} руб.")
        
        try:
            choice = int(input("Выберите фрукт: ")) - 1
            if 0 <= choice < len(fruits):
                fruit = fruits[choice]
                amount = int(input("Количество: "))
                cost = amount * self.price[fruit]['purchase_price']
                
                if cost <= self.money and amount <= self.store[fruit]['max'] - self.store[fruit]['current']:
                    self.money -= cost
                    self.store[fruit]['current'] += amount
                    print(f"Куплено {amount} {fruit} за {cost} руб.")
                else:
                    print("Недостаточно денег или места!")
        except:
            print("Ошибка ввода!")
    
    def next_day(self):
        print(f"\n=== День {self.day} ===")
        
        profit = 0
        for _ in range(randint(5, 15)):
            available = [f for f in self.counter if self.counter[f]['current'] > 0]
            if available and randint(1, 100) <= 70:
                fruit = choice(available)
                self.counter[fruit]['current'] -= 1
                profit += self.price[fruit]['sale_price']
        
        for fruit in self.price:
            change = randint(-2, 2)
            self.price[fruit]['sale_price'] = max(5, self.price[fruit]['sale_price'] + change)
        
        if randint(1, 100) <= 20:
            print("Ашот украл фрукты!")
            for fruit in self.counter:
                stolen = self.counter[fruit]['current'] * randint(50, 100) // 100
                self.counter[fruit]['current'] -= stolen
        
        self.money += profit
        print(f"Заработано: {profit} руб.")
        print(f"Всего денег: {self.money}")
        
        if self.money <= 0:
            print("Банкрот! Игра окончена.")
            return False
        
        if self.day >= 10:
            print("Победа! Вы прожили 10 дней!")
            return False
        
        self.day += 1
        return True
    
    def run(self):
        while True:
            self.show_status()
            
            print("\n1. Перераспределить фрукты")
            print("2. Купить фрукты")
            print("3. Следующий день")
            print("0. Выход")
            
            cmd = input("Выбор: ")
            
            if cmd == '0':
                break
            elif cmd == '1':
                self.redistribute()
            elif cmd == '2':
                self.buy_fruits()
            elif cmd == '3':
                if not self.next_day():
                    break

if __name__ == "__main__":
    name = input("Имя ларька: ")
    game = SimpleFruitStand(name)
    game.run()