"""
В каждом заплыве участвуют два случайных спортсмена из разных сборных.
Напиши программу для печати номеров спортсменов.

1) Программа должна запрашивать количество спортсменов в каждой сборной с сообщением:
«Число участников сборной _:».
2) Затем должна печататься пара случайных спортсменов из разных сборных для заплыва в формате:
«Пловец _ - пловец _».
"""
from random import randint

def print_swimmers(num1, num2):
    swimmer1 = randint(1, num1)
    swimmer2 = randint(1, num2)
    print(f"Пловец {swimmer1} - пловец {swimmer2}")

def swimming_competition():
    num1 = int(input("Число участников сборной 1: "))
    num2 = int(input("Число участников сборной 2: "))
    for i in range(1):
        print_swimmers(num1, num2)

swimming_competition()