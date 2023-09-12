"""
Сохраните информацию из character.json в yaml файл(Имя файла - ваша фамилия)
"""

import json
import yaml

with open("character.json", "r") as file:
    data = json.load(file)

with open("lastname.yaml", "w") as file:
    yaml.dump(data, file)