"""
Выведите из файла character.json Имя персонажа, родную планету и список эпизодов в которых он появлялся.
"""

import json
with open("character.json", "r") as json_file:
    data = json.load(json_file)
    print("Имя персонажа: ", data["name"])
    print("Планета персонажа: ", data["origin"]["name"])
    print("Эпизоды: ", data["episode"])

new_data = {'name': data['name'],
            'planet': data['origin']['name'],
            'episodes:': data['episode']}

with open('new.json', 'w') as new_file:

    json.dump(new_data, new_file, indent=4)