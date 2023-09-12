"""
Напишите программу-имитатор подбрасывания 2 кубиков.
Программа выводит на экран "подбрасываю кубики" и
спустя 2 секунды выводит значения на кубиках в одну строку.
"""
from random import randint
from time import sleep

def roll_dice():
    print("Подбрасываем кубики...")
    sleep(2)
    dice1 = randint(1, 6)
    dice2 = randint(1, 6)
    print(f"Кубик 1: {dice1}  Кубик 2: {dice2}")

roll_dice()