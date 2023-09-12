import random


class Unit:
    def __init__(self, id, team):
        self.id = id
        self.team = team

class Hero(Unit):
    def __init__(self, id, team, level, name):
        super().__init__(id, team)
        self.level = level
        self.name = name
    def lvlup(self):
        self.level += 1

class Soldier(Unit):
    def follow(self, hero):
        print("Солдат", self.id, "следует за героем", hero.name)

Kaplan = Hero(1, 1, 1, "Каплан" )
Areg = Hero(2, 2, 1, "Арег" )

team1 = []
team2 = []
team1.append(Kaplan)
team2.append(Areg)

for i in range(3, 23):
    soldier = Soldier(i, random.randint(1,2)) # рандомно выбираем команду
    if soldier.team == 1:
        team1.append(soldier)
    else:
        team2.append(soldier)

if len(team1) > len(team2):
    Kaplan.lvlup()
else:
    Areg.lvlup()

print("Уровень Каплана:", Kaplan.level, "\nУровень Арега:", Areg.level)
team1[1].follow(team1[0])
for i in team2[1::]: # срез списка от одного до конца
    i.follow(team2[0])


# print("Первая команда: ", team1, "\nВторая команда: ", team2)