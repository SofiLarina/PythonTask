def print_name(name):
    print(name)

fake_name = "Олег"

print_name(fake_name)



def print_name(name):
    return name

fake_name = "Олег"
name1 = print_name(fake_name)
print(name1)


def print_name(name):
    sum_of_numbers = 1000
    print(sum_of_numbers)

fake_name = "Олег"
# print(sum_of_numbers = 1000) не сработает вне функции
name1 = print_name(fake_name)
print(name1)


def print_name(name):
    sum_of_numbers = 1000
    return sum_of_numbers

fake_name = "Олег"
print(sum_of_numbers)
name1 = print_name(fake_name)
print(name1)