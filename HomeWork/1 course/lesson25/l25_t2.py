"""
В классе Hero из предыдущего занятия добавьте приватное свойство rank.
Создайте геттер, сеттер и делиттер чтобы можно было получить звание героя, установить звание "Победитель арены"
в случае победы героя в битве и удалить ранк в случае поражения.
"""
class Hero:
    def __init__(self, name, health, armor, damage):
        self.rank = None
        self.name = name
        self.health = health
        self.armor = armor
        self.damage = damage
    def print_info(self):
        print("Уровень здоровья: ", self.health)
        print("Класс брони: ", self.armor, "\n")

    def get_rank(self):
        return self.rank

    def set_rank(self, rank):
        self.rank = rank

    def del_rank(self):
        del self.rank


class Magician(Hero):
    def hello(self):
        print("Приветствую тебя путник! Я один из учителей магии здесь. Меня зовут", self.name)
        super().print_info()

    def attack(self, enemy: Hero):
        damage = self.damage - enemy.armor
        print(f"Сильный маг атакует {enemy.name} волшебным посохом и наносит ему {damage} урона")
        enemy.health -= damage
        print("Здоровье врага:", enemy.health)
        if enemy.health <= 0:
            enemy.del_rank()
            super().set_rank("Победитель боя")


enemy = Hero("Каплан", 50, 20, 10)
mag = Magician("Арег", 100, 0, 300)
mag.attack(enemy)
print(mag.get_rank())
print(enemy.get_rank())