class Hero:
    def __init__(self, name: str, health: int = 100, attack_power: int = 20):
        self.name = name
        self.health = health
        self.attack_power = attack_power
    
    def strike(self, target: 'Hero') -> None:
        if self.health > 0:
            target.health -= self.attack_power


if __name__ == "__main__":
    knight = Hero("Arthur", 100, 20)
    rogue = Hero("Robin", 80, 15)
    
    knight.strike(rogue)  # Артур бьет Робиннеа
    rogue.strike(knight)  # Робин бьет Артура
    
    print(f"{knight.name}: {knight.health}")
    print(f"{rogue.name}: {rogue.health}")