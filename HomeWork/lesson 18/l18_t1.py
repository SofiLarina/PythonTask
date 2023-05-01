"""
Напишите программу, которая будет спрашивать пользователя ввод имени
пока пользователь не введет off. Программа должна используя lambda-функцию
добавлять к каждому имени надпись "гений".
"""
people = []
while True:
    name = input("Введите своё имя: ")
    if name == "off":
        break
    people.append(name)

genius = list(map(lambda x: x + " гений", people))

print(genius)