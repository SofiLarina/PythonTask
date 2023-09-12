"""
Добавьте на основании классов из презентации класс Magician который наследует Hero.
Со своими методами hello и atack.
"""

class Hero:
    def __init__(self, name, health, armor):
        self.name = name
        self.health = health
        self.armor = armor
    def print_info(self):
        print("Уровень здоровья:", self.health)
        print("Класс брони:", self.armor, "\n")
class Magician(Hero):
    def hello(self):
        print("Приветствую тебя путник! Я один из учителей магии здесь. Меня зовут", self.name)
        self.print_info()
    def attack(self, enemy):
        print("Сильный маг", self.name, "атакует", enemy.name, "волшебным посохом.")
        enemy.armor -= 20
        if enemy.armor < 0:
            enemy.health += enemy.armor
            enemy.armor = 0
        print("Страшный удар обрушился на противника. \nTeперь его броня: " +
        str(enemy.armor) + ", a уровень здоровья: " + str(enemy.health) + "\n")

mag = Magician("Арег", 100, 30)
mag.hello()
enemy = Hero("Каплан", 80, 20)
mag.attack(enemy)




