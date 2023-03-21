"""
Очень часто веб-дизайнеры используют HEX-значение какого-либо цвета.
Напишите программу, принимающую 2 позиционных аргумента: слово "Цвета" и количество цветов
и произвольное количество значений Цвет: HEX. Программа должна вывести все данные на экран.
"""
import random

def generate_hex_colors(color_word, num_colors):
    hex_values = '0123456789ABCDEF'
    colors = {}
    for i in range(int(num_colors)):
        color = ''
        for j in range(6):
            color += random.choice(hex_values)
        colors[f"{color_word} {i+1}"] = f"#{color}"
    return colors

color_word = input("Введите слово для обозначения цветов: ")
num_colors = input("Введите количество цветов: ")

colors = generate_hex_colors(color_word, num_colors)

for color, hex_value in colors.items():
    print(f"{color}: {hex_value}")
