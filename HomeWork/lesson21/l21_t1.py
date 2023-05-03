class Hero: #() можно не писать
    def __init__(self, name, health, armor, power, weapon):
        self.name = name
        self.health = health #если написать 50, то у всех героев этого класса будет 50
        self.armor = armor
        self. power = power
        self.weapon = weapon

    def print_info(self):
        print("Поприветствуйте героя -> ", self.name)
        print("Уровень здоровья: ", self.health)
        print("Уровень брони: ", self.armor)
        print("Уровень силы: ", self.power)
        print("Вооружен -> ", self.weapon)

    def strike(self, enemy):
        print(f"{self.name} ударяет {enemy.name} с помощью {self.weapon}а и наносит урон в размере {self.power}")
        if enemy.armor - self.power <= 0:
            enemy.health += (enemy.armor - self.power) #к enemy.health добавляем и присваивами резьултат
            enemy.armor = 0
        else:
            enemy.armor -= self.power
        print("У врага осталось", enemy.health, "здоровья")

    def fight(self, enemy):
        while self.health > 0 and enemy.health > 0:
            self.strike(enemy)
            enemy.strike(self)
        if self.health < 0 and enemy.health < 0:
            print("Ничья")
        elif self.health < 0:
            print(self.name, "проиграл")
        elif enemy.health < 0:
            print(enemy.name, "проиграл")

name1 = input("Введите имя первого героя: ") #создание экземпляра класса
first_hero = Hero(name1, 500, 50, 100, "Меч")
first_hero.print_info()

name2 = input("Введите имя второго героя: ") #создание экземпляра класса
second_hero = Hero(name2, 400, 100, 150, "Топор")
second_hero.print_info()
#first_hero.strike(second_hero)
#second_hero.strike(first_hero)

first_hero.fight(second_hero)
