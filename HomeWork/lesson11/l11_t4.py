"""
Напишите программу считающую и обрабатывающую индекс массы тела.
В одной функции программа должна считать ИМТ. В другой обрабатывать, если ИМТ ниже 18.5 печатать "Недостаточный вес",
от 18.5 до 25 "ИМТ в норме", больше 25 "Избыточный вес".
Формула определения ИМТ: index = weight / (height * height)
"""
def IMB(weight:int,height:int):
    return weight / (height * height)

def IMB_result(weight:int,height:int):
    result = IMB(weight,height)
    if result >= 25:
        print("Избыточный вес")
    elif  18.5 <= result <= 25:
        print("ИМТ в норме")
    else:
        print("Недостаточный вес")

weight = int(input("Введите ваш вес: "))
height = int(input("Введите ваш рост: "))

IMB_result(weight, height)