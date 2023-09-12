"""
Напишите функцию, которая будет принимать список чисел и выводить на экран надпись
"сегодня x градусов" столько раз сколько значений в списке.
"""
temperatures = [34, 65, 23, 68, 99]

def weather(temperatures):
    for i in temperatures:
        print(f"Сегодня {i} градусов")

weather(temperatures)