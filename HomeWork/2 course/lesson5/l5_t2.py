"""
Из файла info.yaml выведите имя и id Ливерпуля
"""

import yaml

with open("info.yaml", "r") as file:
    data = yaml.safe_load(file)

for pr in data:
    if pr["name"] == "Liverpool":
        print(f"Имя: {pr['name']}", f"ID: {pr['id']}")