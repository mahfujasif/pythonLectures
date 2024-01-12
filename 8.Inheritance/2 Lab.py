# # 1. Write the class Marketer to accompany the other law firm classes
# # described in lecture. Marketers make $50,000 ($10,000 more than general
# # employees) and have an additional method called advertise that prints
# # "Act now, while supplies last!" Make sure to interact with the superclass
# # as appropriate.
#
# class Employee:
#
#     def __init__(self, ini_years):
#         self.__years = ini_years
#
#     def getHours(self):
#         return 40
#
#     def getSalary(self):
#         return 40000
#
#     def getVacationDay(self):
#         return 10 + 2 * self.__years
#
#     def getVacationForm(self):
#         return "yellow"
#
# class Marketer(Employee):
#     def getSalary(self):
#         return super(Marketer, self).getSalary() + 10000
#
#     def getAdvertise(self, s):
#         print(s, "is awesome")
import datetime


# # 2. Write a class HarvardLawyer to accompany the other law firm classes
# # described in the lecture. Harvard lawyers are like normal lawyers, but
# # they make 20% more money than a normal lawyer, they get 3 days more
# # vacation, and they have to fill out four of the lawyer’s forms to go on
# # vacation. That is, the getVacationForm method should return
# # "pinkpinkpinkpink". Make sure to interact with the superclass as
# # appropriate.
#
#
# class Employee:
#
#     def __init__(self, ini_years):
#         self.__years = ini_years
#
#     def getHours(self):
#         return 40
#
#     def getSalary(self):
#         return 40000
#
#     def getVacationDay(self):
#         return 10 + 2 * self.__years
#
#     def getVacationForm(self):
#         return "yellow"
#
#
# class Lawyer(Employee):
#     def getVacationDay(self):
#         return super(Lawyer, self).getVacationDay() + 5
#
#     def getVacationForm(self):
#         return "pinku"
#
#     def getSalary(self):
#         return 50000
#
#
# class HarvardLawyer(Lawyer):
#     def getSalary(self):
#         bs = super(HarvardLawyer, self).getSalary()
#         return bs + 10000
#
#     def getVacationForm(self):
#         return "pinkupinkupinkupinku"
#
# hl = HarvardLawyer(1)
# print(hl.getSalary())


# # 3. Create a VIPBankAccount class based on the above UML notation.
#
# class BankAccount:
#     def __init__(self, aNumber, aName, balance):
#         self.__accountNumber = aNumber
#         self.__accountName = aName
#         self.__balance = balance
#
#     def getAccountNumber(self):
#         return self.__accountNumber
#
#     def getAccountName(self):
#         return self.__accountNumber
#
#     def getBalance(self):
#         return self.__balance
#
#     def depsit(self, amount):
#         self.__balance = self.__balance + amount
#
#     def withdraw(self, amount):
#         if amount <= self.__balance:
#             self.__balance = self.__balance - amount
#             return True
#         return False
#
#
# class VIPBankAccount(BankAccount):
#     def __init__(self, aNumber, aName, balance, cl):
#         super(VIPBankAccount, self).__init__(aNumber, aName, balance)
#         self.__creditLimit = cl
#
#     def getCredit(self):
#         return self.__creditLimit
#
#     def withdraw(self, amount):
#         if amount <= super(VIPBankAccount, self).getBalance():
#             return super(VIPBankAccount, self).withdraw(amount)
#         elif amount <= super(VIPBankAccount, self).getBalance() + self.__creditLimit:
#             self.__creditLimit = self.__creditLimit - (amount - super(VIPBankAccount, self).getBalance())
#             return super(VIPBankAccount, self).withdraw(super(VIPBankAccount, self).getBalance())
#         else:
#             return False


# 5. Create consider the task of representing types of tickets to campus events.
# Each ticket has a unique number and a price. There are three types of
# tickets: walk-up tickets, advance tickets, and student advance tickets.
# Figure.1 illustrates the types:

class Ticket:
    event = datetime.datetime(2024, 1, 15, 14)

    def __init__(self, number):
        self.__number = number
        self.__price = 50

    def getNumber(self):
        return self.__number

    def getPrice(self):
        return 50


class WalkTicket(Ticket):
    def __init__(self, nm):
        super().__init__(nm)

    def getNumer(self):
        return super(WalkTicket, self).getNumber()

    def getPrice(self):
        return super(WalkTicket, self).getPrice()


class AdTicket(Ticket):
    def __init__(self, nm):
        super().__init__(nm)
    
    def getNumer(self):
        return super(AdTicket, self).getNumber()

    def getPrice(self):
        df = Ticket.event - datetime.datetime.now()
        op = super(AdTicket, self).getPrice()
        if df.days > 10:
            return op - 20
        return op - 10


class StuTicket(AdTicket):
    def __init__(self, nm):
        super().__init__(nm)

    def getNumer(self):
        return super(StuTicket, self).getNumber()

    def getPrice(self):
        op = super(StuTicket, self).getPrice()
        return op / 2
