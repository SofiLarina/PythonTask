nik_name = list(input('Введите логин:'))
for i in nik_name:
    if i not in '1234567890qwertyuiopasdfghjklzxcvbnm':
        print('Неверный символ:', i)
        break
else:
    print('Вы зарегистрированы!')