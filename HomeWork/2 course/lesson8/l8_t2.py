"""
Напишите скрипт который получает системный ввод от пользователя и
выводит надпись "команда принята" если ввод начинается с sys.in.
"""
import sys

user_input = sys.stdin.readline().strip()

if user_input.startswith("sys.in"):
    print("Команда принята")
else:
    print("Команда не начинается с sys.in")