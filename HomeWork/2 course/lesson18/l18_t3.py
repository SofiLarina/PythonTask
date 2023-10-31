"""
Создайте функцию в демоне потока которая каждые 3 секунды будет писать "Вводите быстрее".
В основной части программы запросите ввод кода от бомбы и если код неверный
выведите: "Вы взорвались", если верный - "Бомба разминирована"
"""
from time import sleep
from threading import Thread

def speed():
    while True:
        print("\nВводите быстрее\n")
        sleep(3)

speed_thread = Thread(target=speed)

def bomb():
    code = input("Введите код от бомбы: ")
    if code == "12345":
        print("Бомба разминирована")
    else:
        print("Вы взорвались")

speed_thread.daemon = True
speed_thread.start()
bomb()