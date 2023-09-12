"""
Описание классовой структуры. Есть Человек, характеристиками которого являются:
Имя, Возраст, Наличие денег, Наличие собственного жилья.
Человек может: Предоставить информацию о себе, Заработать деньги, Купить дом
Также есть Дом, к свойствам которого относятся: Площадь, Стоимость
Для Дома можно: Применить скидку на покупку
"""

class Human:
    def __init__(self, name, age, money, house):
        self.name = name
        self.age = age
        self.money = money
        self.house = house

    def info(self):
        print("Меня зовут", self.name, "Мой дом:", self.house)

    def earn(self, salary):
        self.money += salary

    def buy_house(self, clhouse):
        if self.house == False and self.money >= clhouse.cost:
            clhouse.discount(10)
            self.house = True
            self.money -= clhouse.cost
        elif self.house == True:
            print("У вас уже есть дом :)")
        elif self.money < clhouse.cost:
            print("У вас не хватает денег :(")

class House:
    def __init__(self, square, cost):
        self.square = square
        self.cost = cost

    def discount(self, value):
        self.cost = self.cost/100*value

sigma = House(100, 1000000)
kaplan = Human("Каплан", 12, 0, False)
kaplan.info()
kaplan.earn(1000000000000)
kaplan.buy_house(sigma)
kaplan.info()