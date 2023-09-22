"""
Напишите программу, которая создает папку task4 и записывает
текст "я выполнил задание" в файл answer.txt
"""
import os

os.mkdir("task4")
with open(r"task4/answer.txt", "w") as file:
    file.write("Я выполнила задание! :з")
