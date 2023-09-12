marks = []
mark = int(input("Введите оценки: "))
while mark != 6:
    marks.append(mark)
    mark = int(input("Введите оценки: "))
number = len(marks)
five = marks.count(5)
print((five / number) * 100)
