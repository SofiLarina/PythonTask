# Класс животного, экземпляр с видом, вывод голоса животного
class Animal:
    def __init__(self, voice, type):
        self.type = type
        self.voice = voice
    def make_voice(self):
        print("Голос животного: ", self.voice)
    def fight(self, other):
        print(self.type, "атакует", other.type)

dog = Animal("Гав", "Овчарка")
dog.make_voice()
print("Тип животного: ", dog.type)

cat = Animal("Мяу", "Оцикет")
cat.make_voice()
print("Тип животного: ", cat.type)

dog.fight(cat)
