"""
На летней универсиаде будет проводиться по два забега. Чтобы соревнования были честными,
участники должны распределяться между забегами случайным образом.
Напишите программу, печатающую случайные номера забегов (1 или 2) до тех пор,
пока не будет введено «off».
После генерации каждого номера должно печататься:
1) «Ваш номер: _».
2) «Участников в первом забеге: _», «Участников во втором забеге: _».
"""
from random import randint

def print_race(num1, num2):
    race = randint(1, 2)
    print(f"Ваш номер: {race}")
    if race == 1:
        print(f"Участников в первом забеге: {num1}, Участников во втором забеге: {num2}")
    else:
        print(f"Участников в первом забеге: {num2}, Участников во втором забеге: {num1}")

def racing_competition():
    num1 = int(input("Число участников в первом забеге: "))
    num2 = int(input("Число участников во втором забеге: "))
    while True:
        user_input = input("Введите 'off' для выхода или любую другую клавишу для продолжения: ")
        if user_input == "off":
            break
        print_race(num1, num2)

racing_competition()