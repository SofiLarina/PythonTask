# Является ли слово палиндромом
word = input("Введите слово: ").lower()
reversed_word = word[::-1]
if word == reversed_word:
    print("Палиндром")
else:
    print("Не палиндром")