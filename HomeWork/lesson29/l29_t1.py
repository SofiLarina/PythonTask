"""
 Есть Помидор со следующими характеристиками: Индекс,
 стадия зрелости(стадии: Отсутствует, Цветение, Зеленый, Красный).
 Помидор может: Расти(переходить на следующую стадию зрелости),
 предоставлять информацию о своей зрелости(магический метод str). Есть куст с помидорами,
 который: Содержит список помидоров которые на нем растут. И может: Расти(добавляя томат).
 Предоставлять информацию о зрелости всех томатов на нем, предоставлять
 урожай(убирать с себя все красные помидоры). И также есть садовник, который имеет: Имя,
 куст за которым ухаживает. И может: Ухаживать за кустом(выводить информацию о зрелости
 всех его помидоров), собирать урожай с куста. Реализуйте соответсвующие классы и
 продемонстрируйте работу.
"""

class Tomato:
    def __init__(self, index, maturity):
        self.index = index
        self.maturity = ["Отсутствует", "Цветение", "Зеленый", "Красный"]
        self.current = maturity

    def grow(self):
        self.current += 1
        if self.current >= 3:
            self.current = 3

    def __str__(self):
        return self.maturity[self.current]

class Bush:
    def __init__(self):
        self.tomatoes = []

    def bush_grow(self, tomato):
        self.tomatoes.append(tomato)

    def bush_info(self):
        for tomato in self.tomatoes:
            print(tomato)

    def harvest(self):
        for tomato in self.tomatoes:
            if tomato.current == 3:
                self.tomatoes.remove(tomato)

class Gardener:
    def __init__(self, name):
        self.name = name
        self.bushes = []

    def bushes_info(self):
        for bush in self.bushes:
            bush.bush_info()

    def harvesting(self):
        for bush in self.bushes:
            bush.harvest()

Kaplan = Gardener("Каплан")

bush1 = Bush()
bush2 = Bush()

Areg = Tomato(0, 0)
Karina = Tomato(1, 3)
Arnou = Tomato(2, 2)
Lesha = Tomato(3, 0)

print("Стадия помидора Арег:", Areg)
Areg.grow()
print("Стадия помидора Арег:", Areg)

print("Стадия помидора Карина:", Karina)
Karina.grow()
print("Стадия помидора Карина:", Karina)

bush1.bush_grow(Karina)
bush1.bush_grow(Areg)
bush2.bush_grow(Arnou)
bush2.bush_grow(Lesha)

Kaplan.bushes.extend([bush1, bush2])
print("Все помидоры до сбора:")
Kaplan.bushes_info()

Kaplan.harvesting()
print("Помидоры после сбора:")
Kaplan.bushes_info()



