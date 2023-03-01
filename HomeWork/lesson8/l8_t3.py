"""
Напишите программу принимающую ввод информации о треке(место в чарте,исполнитель, название) пока пользователь
не введет "off". Программа должна вывести всю информацию в виде словаря вида: {(место,испонитель): название трека}
"""

songs = dict()
place = input('Введите место трека в чарте: ')
singer =  input('Введите исполнителя трека: ')
name = input('Введите название трека: ')
while place != 'off' and singer != 'off' and name != 'off':
    songs[(place, singer)] = name
    place = input('Введите место трека в чарте: ')
    if place == 'off':
        break
    singer = input('Введите исполнителя трека: ')
    if singer == 'off':
        break
    name = input('Введите название трека: ')
    if name == 'off':
        break
print(songs)

