full_name = input()
a = ""

a += full_name[:full_name.find(" ")] + " "

full_name = full_name[full_name.find(" ") + 1:]
a += full_name[0] + "."

full_name = full_name[full_name.find(" ") + 1:]
a += full_name[0] + "."

print(a)