"""
Создайте класс SpaceObject у которого будут свойство размер.
Создайте 2 класса Star и Planet которые будут наследовать SpaceObject.
В классе Star добавьте свойство яркость и метод светить в котором будет
выводится на экран с какой яркостью светит звезда.
Классу Planet добавьте свойства население и прирост за год и метод
который будет печатать население через переданное ему количество лет.
"""


class SpaceObject:
    def __init__(self, size):
        self.size = size


class Star(SpaceObject):
    def __init__(self, size, light):
        super().__init__(size)
        self.light = light

    def show_light(self):
        print("Звезда светит с яркостью", self.light)


class Planet(SpaceObject):
    def __init__(self, size, population, growth):
        super().__init__(size)
        self.population = population
        self.growth = growth

    def calculate(self, years):
        print("Население планеты через переданное количество лет будет равняться", (self.population + (self.growth * years)))


sun = Star(100, 500)
sun.show_light()
earth = Planet(10, 1000000, 5000)
earth.calculate(5)