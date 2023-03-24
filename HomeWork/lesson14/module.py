def router(request):
    if "расп" in request:
        timetable()
    elif "трен" in request:
        trainer()
    elif "оплат" in request:
        payment()
    elif "меню" in request:
        menu()
    elif "тест" in request:
        tests()
    else:
        print("Вы ввели некорректный запрос")

def timetable():
    print("Расписание занятий сегодня: йога, футбол, волейбол")
def trainer():
    print("Контактные данные тренера: Крдян Арег +79549711288")
def payment():
    print("Сумма к оплате занятия: 3000 р.")
def menu():
    print("Меню в столовой сегодня: пюре, котлета, помидор")
def tests():
    print("Сегодня тесты по: алгебре, русскому")