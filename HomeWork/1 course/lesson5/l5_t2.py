summa = int(input('Введите сумму к оплате:'))
time = int(input('Введите время:'))
if 10 < time < 12:
    print('Сумма к оплате:', summa/2)
elif 20 < time < 22:
    print('Сумма к оплате:', summa/4)
else:
    print('Магазин не работает сейчас')