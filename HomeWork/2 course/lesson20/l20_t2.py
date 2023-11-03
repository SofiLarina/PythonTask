"""
Напишите 2 функции
Первая должна принимать ширину, длинну и высоты комнаты и записывать в файл площадь комнаты из 4 стен.
Вторая должна записать в тот же файл расход краски исходя из соотношения 5л/кв.м.
"""
def calculate_room_area(width, length, height):
    area = 2 * (width * height + length * height)
    return area

def calculate_paint_usage(area):
    paint_usage = area * 5
    return paint_usage

if __name__ == "__main__":
    width = 4
    length = 5
    height = 3

    room_area = calculate_room_area(width, length, height)
    paint_usage = calculate_paint_usage(room_area)

    """
    with open("room_data.txt", "w") as file:
        file.write(f"Площадь комнаты: {room_area} квадратных метров\n")
        file.write(f"Расход краски: {paint_usage} литров")
    """


    with open("room_data.txt", "w") as file:
        file.write(f"Room area: {room_area} square meters\n")
        file.write(f"Paint usage: {paint_usage} liters")