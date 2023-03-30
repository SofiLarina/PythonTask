"""
1 функция - принимает имя и количество положительных оценок
 и заносит в словарь ключ-имя значение-количество оценок
2 функция принимает строку/имя и выводит количество оценок
"""
grades_dict = {}
def student(name, grades):
    grades_dict[name] = grades
def print_grades(name):
    if name in grades_dict:
        print(f"{name} имеет {grades_dict[name]} положительных оценок.")
    else:
        print(f"{name} нет оценок.")
student("Арег", 5)
print_grades("Арег")