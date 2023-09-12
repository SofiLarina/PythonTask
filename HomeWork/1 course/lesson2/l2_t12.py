import math
a = float(input('Введите ширину поверхности:'))
b = float(input('Введите высота поверхности:'))
expenditure = float(input('Введите расход краски:'))
liters_bottles = float(input('Введите объём банки в литрах:'))
percent = float(input('Введите процент запаса:'))

square = a * b
print('Площадь окрашивания:', (round(a * b, 2)))

liters = square / expenditure
unused = liters * percent / 100
liters += unused
print('Количество литров:', (round(liters, 2)))

bottles = int(math.ceil(liters / liters_bottles))
print('Количество банок:', (bottles))


print('Неиспользуемые литры краски:', (round((float(bottles) * liters_bottles) - liters, 2)))