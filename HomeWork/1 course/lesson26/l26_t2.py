"""
Создать базовый класс ОЛИМПИАДНЫЕ ЗАДАНИЯ (данные об участнике, количество тестовых примеров,
количество пройденных тестов).
Создать производные классы ЗАДАНИЯ «ВСЕ ИЛИ НИЧЕГО»
(задается максимальное количество баллов за задание (даются только когда все тесты пройдены)
и ЗАДАНИЯ «ЧЕМ БЫСТРЕЕ, ТЕМ ЛУЧШЕ» (задается время участника на решение,
лучшее время всех участников, максимальное количество баллов за задание,
процент снижения балла в минуту отставания от лучшего времени).
Для заданных примеров задач, которые решали участники,
упорядочить участников по росту набранных баллов и определить суммарное количество баллов,
набранных заданным участником олимпиады.
Для проверки использовать действия над списком,
в котором разместить объекты разных производных классов.
"""

class OlympiadTasks:
    def __init__(self, person, examples, tests):
        self.person = person
        self.examples = examples
        self.tests = tests

    def calculate(self):
        pass

class AllorNothing(OlympiadTasks):
    def __init__(self, person, examples, tests, max):
        super().__init__(person, examples, tests)
        self.max = max

    def calculate(self):
        if self.tests == self.examples:
            return self.max
        else:
            return 0

class FasterIsBetter(OlympiadTasks):
    def __init__(self, person, examples, tests, time, best_time, max, percent):
        super().__init__(person, examples, tests)
        self.time = time
        self.best_time = best_time
        self.max = max
        self.percent = percent

    def calculate(self):
        if self.time <= self.best_time:
            return self.max
        else:
            time_difference = self.time - self.best_time
            point_reduction = time_difference * self.percent
            score = self.max - point_reduction
            if score < 0:
                return 0
            else:
                return score

Kaplan = AllorNothing("Каплан", 3, 3, 10)
Areg = FasterIsBetter("Арег", 5, 4, 120, 100, 20, 2)
result = [Kaplan, Areg]

sorted = sorted(list, key=lambda x: x.calculate(), reverse = True)

total_score = sum(task.calculate() for task in list if task.person == "Каплан")

print(total_score)