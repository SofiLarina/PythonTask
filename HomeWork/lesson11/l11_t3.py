"""
Напишите программу определяющую допуск ученика к зачету.
Программа должна запрашивать число учеников, затем у каждого ученика запрашивать балл за финальный тест
и в ответ печатать, допущен ли он (True или False) к зачету (необходимо набрать больше 50 баллов).

Ученикам без допуска должно печататься "Вы отчислены".

Выдачу допуска реализуй как функцию.
"""

def mark_test(mark):
    return mark > 50

amount = int(input("Число учеников: "))
for i in range(amount):
    mark1 = int(input("Введите балл за тест: "))
    result = mark_test(mark1)
    if result:
        print("Вы молодец!")
    else:
        print("Вы отчислены :(")


