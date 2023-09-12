from module import router
while True:
    request = str(input("Введите ваш запрос: ")).lower()
    router(request)