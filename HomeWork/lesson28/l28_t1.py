"""
Создайте композицию User состояющую из:
Объекта Profile со свойствами: name,last_name,age,pasport и методом print_info.
Объекта Address со свойствами : City,street,zipcode
Объекта Role со свойствами: role,hours_worked
Объекта BankAccount со свойствами: card_number, balance
Объекта Order с методом устанавливающими параметры заказа: Item,date,delivery,price
Добавьте в композицию методы создания профиля, установки адреса,
роли, привязки банковского аккаунта и добавления заказа
"""
from datetime import datetime

class Profile:
    def __init__(self, name, last_name, age, passport):
        self.name = name
        self.last_name =last_name
        self.age = age
        self.passport = passport

    def print_info(self):
        print(f"ФИ: {self.last_name} {self.name}\nВозраст: {self.age}\nПаспорт: {self.passport}")

class Address:
    def __init__(self, city, street, zipcode):
        self.city = city
        self.street = street
        self.zipcode = zipcode

class Role:
    def __init__(self, role, hours_worked):
        self.role = role
        self.hours_worked = hours_worked

class BankAccount:
    def __init__(self, card_number, balance):
        self.card_number = card_number
        self.balance = balance

class Order:
    def __init__(self):
        self.item = None
        self.date = None
        self.delivery = None
        self.price = None

    def confirm_order(self, item, delivery, price):
        self.item = item
        self.date = datetime.now()
        self.delivery = delivery
        self.price = price

class User:
    def __init__(self):
        self.profile = None
        self.address = []
        self.role = []
        self.bank = []
        self.order = []

    def set_profile(self, name, last_name, age, passport):
        self.profile = Profile(name, last_name, age, passport)
        self.profile.print_info()

    def set_address(self, city, street, zipcode):
        self.address.append(Address(city, street, zipcode))

    def set_role(self, role, hours_worked):
        self.role.append(Role(role, hours_worked))

    def set_bank(self, card_number, balance):
        self.bank.append(BankAccount(card_number, balance))

    def set_order(self, item, delivery, price):
        self.order.append(Order())
        for order in self.order:
            order.confirm_order(item, delivery, price)

    def show_city(self):
        for i in self.address:
            print("Город:", i.city)

