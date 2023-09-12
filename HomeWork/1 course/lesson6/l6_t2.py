a = input('Введите режим(off - завершить):').lower()
while a == 'game':
    print('Запуск игры угадай число')
    number = int(input('Введите число:'))
    while number != 5:
        print('Подумай еще!')
        number = int(input('Введите число:'))
    print('Вы угадали!')
    break
print('Игра окончена')

