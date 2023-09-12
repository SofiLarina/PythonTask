"""
В быстрых шахматах на принятие решений для всех ходов игроку даётся 30 минут. Программа должна:
Предлагать ввод хода (например, E2–E4) и считать потраченное время.
После получения хода печатать оставшееся время в минутах.
Если 30 минут закончились или игрок вводит «off» — завершать работу.
Оформить в виде функции.
"""
from time import time
def chess():
    start = time()
    remaining = 30
    while remaining > 0:
        move = input("Введите свой ход: ")
        if move == "off":
            break
        elapsed = int(time() - start) // 60
        remaining = 30 - elapsed
        print(f"Осталось времени: {remaining} минут")
    print("Игра завершена")

chess()

"""
from time import time

def chess():
    remaining = 30
    move = input("Введите свой ход: ")
    start = time()
    while remaining > 0 and move != "off":
        move = input("Введите свой ход: ")
        end = time()
        move_time = end - start
        left = left - move_time
        print(f"Осталось времени: {left}")
chess()
"""


