"""
Создайте класс Person у которого будут свойства name и age.
Добавьте метод экземпляра который выводит информацию о человеке.
Создайте метод класса который генерирует новый объект класса
который ставить возраст человека: сегодняшний год - год который передают в метод.
(подсказка: тут можно использовать метод today().year класса date из модуля datetime)
Создайте статический метод который проверяет является ли совершеннолетним человек
возраст которого передается в метод.
"""
import datetime
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"Имя: {self.name}\nВозраст: {self.age}")

    @classmethod
    def newKaplan(cls, year):
        return Person("Каплан", datetime.datetime.today().year - year)

    @staticmethod
    def check(year):
        return True if year >= 18 else False

Areg = Person("Арег", 16)
Areg.info()

Kaplan = Person.newKaplan(2006)
Kaplan.info()

print(Kaplan.check(19))