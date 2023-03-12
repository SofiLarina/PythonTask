# Есть ли повторяющиеся элементы в строке. Вывести True False
a = input("Введите: ")
b = set(a)
if len(a) != len(b):
    print(False)
else:
    print(True)