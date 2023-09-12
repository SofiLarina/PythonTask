text = input('').split('@')
last = text[0].split()[-1]
first = text[1].split()[0]
print(last + '@' + first)