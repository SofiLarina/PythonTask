category = str(input('Введите категорию товара:'))
summa = int(input('Введите цену товара:'))
if category == 'Продукты':
    if summa < 100:
        print('Попробуйте нашу выпечку!')
    elif 100 <= summa < 500:
        print('Как насчёт орехов в шоколаде?')
    else:
        print('Попробуйте экзотические фрукты!')
else:
    print('Загляните в товары для дома!')