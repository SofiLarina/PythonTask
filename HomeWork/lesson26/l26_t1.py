"""
Создайте классы утка и человек. У обоих классов нету свойств,
но есть методы крякать и носить одежду. Утка крякает, а человек имитирует кряканье.
Добавьте экземпляры этих классов в список и вызовите в цикле соответствующие методы.
"""
class Human:
    def quack(self):
        print("Типо кря кря")
    def wear(self):
        print("Носить одежду")

class Duck:
    def quack(self):
        print("Кря кря")
    def wear(self):
        print("Носить уточную одежду")

Areg = Human()
Kaplan = Duck()
animals = [Areg, Kaplan]

for animal in animals:
    animal.quack()
    animal.wear()