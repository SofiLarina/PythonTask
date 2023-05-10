class Student:
    def __init__(self, name, mark):
        self.name = name
        self.mark = mark
        self.course = "-"
    def set_course(self, new_course):
        self.course = new_course
        print("Для студента ", self.name, "установлен курс", self.course)
    def print_info(self):
        if self.mark < 50:
            print(self.name, "на грани отчисления")
        else:
            print(self.name, "в порядке")

Kaplan = Student("Каплан", 20)
Kaplan.set_course(1)
Kaplan.print_info()

Areg = Student("Арег", 100)
Areg.set_course(2)
Areg.print_info()