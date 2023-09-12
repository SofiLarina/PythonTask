# Список дней недели, сделать словарь ключ - день недели, номер этого дня - значение
weekend = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
counter = 1
dict_weekend = dict()
for i in weekend:
    dict_weekend[i] = counter
    counter += 1
print(dict_weekend)
print(dict_weekend["Среда"])
