marks = []
mark = int(input("Введите оценки: "))
while mark != 6:
    marks.append(mark)
    mark = int(input("Введите оценки: "))
number = len(marks)
three = marks.count(3)
four = marks.count(4)
five = marks.count(5)
print((three + four + five) / number * 100)
