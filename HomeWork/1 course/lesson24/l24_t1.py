class Work:
    def __init__(self, place):
        self.place = place
    def work_info(self):
        print("Место работы:", self.place)

class Workings_student(Work):
    def __init__(self, place, name, study):
        super().__init__(place)
        self.name = name
        self.study = study
    def student_info(self):
        self.work_info() # если хотим обратиться к методу из класса еще раз, можно вызвать с помощью self
        print("Место учебы:", self.study, "\nИмя студента:", self.name)

student = Workings_student("Россети", "Арег", "Колледж Сириус")
student.student_info()