numbers = input("Введите числа:")
numbers = [int(x) for x in numbers.split()]
len = len(numbers)

if len == 1:
    print("Нет")
elif sorted(numbers) == numbers:
    print("Да")
else:
    print("Нет")
