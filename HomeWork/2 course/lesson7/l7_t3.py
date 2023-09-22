"""
Напишите программу-вирус которая переименовывает папки c четными номерами в
ранее созданной папке target, новые имена придумайте самостоятельно.
"""
import os

for i in range(2, 11, 2):
    folder_name = "target/" + str(i)
    new_name = "target/Kaplan.6" + str(i)
    os.rename(folder_name, new_name)