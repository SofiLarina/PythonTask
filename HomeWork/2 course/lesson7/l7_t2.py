"""
Создайте программу создающую папку target внутри которой еще
10 папок имена которых цифры от 1 до 10
"""

import os

os.mkdir("target")

for i in range(1, 11):
    folder = "target/" + str(i)
    os.mkdir(folder)