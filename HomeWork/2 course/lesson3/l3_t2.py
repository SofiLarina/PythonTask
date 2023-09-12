"""
Сохраните данные из списка в json файл(Имя файла - ваша фамилия и номер задания) с отступом 4, формата:
name: ***
age: ***
countries: ***
"""
task = ["oleg",24,["Belarus","Russia"]]

import json
dict = {"name": task[0],
        "age": task[1],
        "countries": task[2][0]}

with open("file.json", "w") as json_file:
    json.dump(dict, json_file, indent=4)