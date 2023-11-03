"""
Напишите функцию которая через канал обмена возвращает количество валюты которую можно приобрести на n сумму денег при курсе 1 к 75.
Запустите функцию в отдельном процессе и отправьте в нее данные задержкой в 0.5 секунды передайте ей разное количество доступных денег.
Выводите количество валюты на экран по мере обработки данных.
"""
import multiprocessing
from time import sleep


def exchangecurrency(conn):
    exchangerate = 75
    while True:
        money = conn.recv()
        if money is None:
            break
        currency = money / exchangerate
        conn.send(currency)


def main():
    parentconn, childconn = multiprocessing.Pipe()
    currency_process = multiprocessing.Process(target=exchangecurrency, args=(childconn,))
    currency_process.start()

    sleep(0.5)

    money1 = 1000
    money2 = 500
    parentconn.send(money1)
    parentconn.send(money2)
    parentconn.send(None)

    for i in range(2):
        currency = parentconn.recv()
        print("Количество валюты:", currency)

    currency_process.join()


if __name__ == "__main__":
    main()
