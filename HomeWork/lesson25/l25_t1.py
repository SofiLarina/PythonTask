"""
Создайте класс банковского аккаунта по аналогии с примером из презентации.
Сделайте атрибут name защищенным, а balance и pasport приватными.
Добавьте геттер-методы на pasport и balance. Сделайте смену номера паспорта по поролю.
А изменение баланса на определенную сумму(сумма не может падать меньше 0,
так что сделайте проверку). Создайте метод удаляющий паспортные данные с аккаунта(также по поролю).
"""
class BankAccount:
    def __init__(self, name, balance, passport, password):
        self._name = name
        self.__balance = balance
        self.__passport = passport
        self.__password = password
    def get_passport(self):
        return self.__passport
    def get_balance(self):
        return self.__balance
    def set_passport(self, password, new_passport):
        if password == self.__password:
            self.__passport = new_passport
        else:
            print("Пароль введен не верно. Вы не", self._name)
    def set_balance(self, new_balance):
        if self.__balance + new_balance < 0:
            print("Недостаточно средств")
        else:
            self.__balance += new_balance
    def del_passport(self):
        if password == self.__password:
            del self.__passport
        else:
            print("Пароль введен не верно. Вы не", self._name, ".")

Ac1 = BankAccount("Каплан", 10, "7777 7777", 1234567)
Ac1.set_balance(1000)
Ac1.set_balance(-100)
print("Ваш баланс:", Ac1.get_balance())

Ac1.set_passport("1111 1111", 7654321)
print(Ac1.get_passport())

Ac1.del_passport("1234567") # ошибка должна быть
print(Ac1.get_passport())