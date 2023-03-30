"""
Надежность пароля
"""
password = input("Введите пароль: ")

def password_strong(password):
    if len(password) >= 8 and password.lower() != password:
        return True
    else:
        return False
print(password_strong(password))