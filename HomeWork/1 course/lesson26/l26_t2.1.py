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

class AllorNothing(OlympiadTasks):
    def __init__(self, person, examples, tests, max):
        super().__init__(person, examples, tests)
        self.max = max

class FasterIsBetter(OlympiadTasks):
    def __init__(self, person, examples, tests, time, best_time, max, percent):
        super().__init__(person, examples, tests)
        self.time = time
        self.best_time = best_time
        self.max = max
        self.percent = percent

task1 = AllorNothing("Каплан", 10, 1, 0)
task2 = AllorNothing("Арег", 10, 10, 10)
task3 = FasterIsBetter("Арноу", 10, 3, 0, 60, 25, 10)
task4 = FasterIsBetter("Карина", 10, 9, 0, 73, 30, 10)

result = [task1, task2, task3, task4]
for task in result:
    print(Task.max())
