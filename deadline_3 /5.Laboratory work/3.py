class Animal:
    def __init__(self, name: str):
        self.name = name
    
    def make_sound(self) -> None:
        print("Животное издает звук")


class Dog(Animal):
    def make_sound(self) -> None:
        print("Гав!")


class Cat(Animal):
    def make_sound(self) -> None:
        print("Мяу!")


def animal_chorus(animals: list) -> None:
    for animal in animals:
        animal.make_sound()


if __name__ == "__main__":
    animals = [Dog("Гарик"), Cat("Воля")]
    animal_chorus(animals)