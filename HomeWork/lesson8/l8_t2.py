"""
Дана строка чисел от 0 до 9 необходимо создать словарь где в качестве ключа будет цифра,
а в качестве значения количество этих цифр в строке
"""
numbers = "0139412831055230677798"
dict_of_numbers = dict()
for i in range(0, 10):
    dict_of_numbers[i] = numbers.count(str(i))
print(dict_of_numbers)
