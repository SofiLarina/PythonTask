numbers = []
while True:
    num = input("Введите число: ")
    if num == "":
        break
    numbers.append(int(num))
arg = sum(numbers)/len(numbers)
# except ZeroDivisionError:
#     print("Вы ничего не ввели")
print("Среднее арифметическое: ", arg)

bta = []
lta = []
eta = []
# for i in numbers:
#     if i > arg:
#         bta.append(i)
#     elif i < arg:
#         lta.append(i)
#     else:
#         eta.append(i)

bta:[i for i in numbers if i > arg]
lta:[i for i in numbers if i < arg]
eta:[i for i in numbers if i == arg]

print("Больше среднего: ", bta)
print("Меньше среднего: ", lta)
print("Равно среднему: ", eta)