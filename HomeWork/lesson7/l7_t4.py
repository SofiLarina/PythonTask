teachers = []
a = input("Записать нового учителя(да/нет)? ").lower()

while a != 'нет':
    teacher = []
    if a == 'да':
        teacher.append(input("Фамилия преподавателя: "))
        teacher.append(input("Должность преподавателя: "))
        teacher.append(input("Количество студентов во всех группах(например: 12,8,10): "))
        teachers.append(teacher)
    print(teachers)
    a = input("Записать нового учителя(да/нет)? ").lower()

