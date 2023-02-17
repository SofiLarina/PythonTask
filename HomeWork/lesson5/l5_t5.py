num = int(input('Введите число:'))
if (num%10)%2==0:
    if (sum(map(int, str(num))))%3 == 0:
        print('Число делится на 6')
else:
    print('Число не делится на 6')