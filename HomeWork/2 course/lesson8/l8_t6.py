import sys
a = sys.stdin.readline()

if sys.argv[0] == "-r":
    print("Флаг передан, работаем рекурсивно", sys.argv[2])
else:
    print("Обычная работа скрипта с параметром", sys.argv[1])