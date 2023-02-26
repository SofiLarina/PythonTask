summa = int(input('Введите сумму к оплате:'))
while True:
    cost = float(input('Введите стоимость покупки: '))
    if cost % 2 == 0:
        cost = cost / 2
        print('К оплате: ', cost)
    else:
        cost = (cost / 100) * 15
        print('К оплате:', cost)

    print('Спасибо за покупку!')
