"""
Сохраните данные из списка в json файл(Имя файла - ваша фамилия и номер задания) с отступом 4, формата:
name: ***
age: ***
countries: [
{
name:***
time:***
cities:***
}
]
"""
import json
task = ["oleg",24,["Belarus", "Russia"],(24,1),["Moscow", "Vladikavkaz", "Krasnodar", "Rostov", "Nalchik"]]

data = {'name': task[0], "age": task[1],
        "countries":[{"name": task[2][0],
        "time": task[3][0], "cities": task[4][2]},
        {"name": task[2][1], "time": task[3][1], "cities": task[4][0]}]}


with open("file1.json", "w") as json_file:
    json.dump(data, json_file, indent=4)