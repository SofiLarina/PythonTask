"""
Запустите фоновый процесс который следит за сроком подписки пользователя( для примера 10 секунд) если время подписки вышло выведите надпись "Ваша подписка закончилась."
и завершите работу программы. В основной программе сыграйте с пользователем в игру "угадай число".
"""
from random import randint
import multiprocessing
from time import sleep

def check_subscription(subscription_duration):
    sleep(subscription_duration)
    print("Ваша подписка закончилась")
    exit()

def play_guessing_game():
    secret_number = randint(1, 10)
    guess = None
    while guess != secret_number:
        guess = int(input("Угадайте число от 1 до 10: "))
        if guess < secret_number:
            print("Загаданное число больше")
        elif guess > secret_number:
            print("Загаданное число меньше")
        else:
            print("Поздравляю! Вы угадали")

def main():
    subscription_duration = 10
    subscription_process = multiprocessing.Process(target=check_subscription, args=(subscription_duration,))
    subscription_process.start()
    play_guessing_game()
    subscription_process.terminate()
    subscription_process.join()

if __name__ == "__main__":
    main()