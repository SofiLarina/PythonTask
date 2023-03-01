a = input()
b = ""
for i in a:
    try:
        int(i)
        b += i
    except:
        pass
print(b)