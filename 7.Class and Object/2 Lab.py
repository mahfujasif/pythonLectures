# # 1.Complete the Point class we discussed in the lecture.
# #
# # 2.Add the following method to the Point class:
# # def isVertical(self,p):
# # where p is another Point. The method returns true if the given Point lines up vertically with
# # the current Point, that is, if their x-coordinates are the same.
# #
# # 3.
# # Add the following method to the Point class:
# # def slope(self, p):
# # where p is another Point and the method returns the slope of the line drawn between this Point and the
# # given other Point. Use the formula (y2-y1)/(x2-x1) to determine the slope between (x1,y1) and (x2,y2).
#
# import math
#
#
# class Point:
#     status = "OK"
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def getX(self):
#         return self.__x
#     def getY(self):
#         return self.__y
#
#     def setX(self, x):
#         self.__x = x
#     def setY(self, y):
#         self.__y = y
#
#     @staticmethod
#     def checkStatus():
#         print("Status:", Point.status)
#
#     def printCord(self):
#         print(self.__x, ":", self.__y)
#
#     def __validate(self):
#         print("Validating point", self.__x, ",", self.__y)
#
#     def distance(self, x2, y2):
#         self.__validate()
#         return math.sqrt(((self.__x-x2)**2) + ((self.__y-y2)**2))
#
#     def isVertical(self, p):
#         return self.__x == p.__x
#
#     def slope(self, p):
#         return (p.__y - self.__y)/(p.__x - self.__x)
#
#
# p = Point(10,15)
# p.checkStatus()
# p.printCord()
# print(p.distance(11, 20))
#
# print("Vertical:", p.isVertical(Point(10,15)))
#
# print("Slop:", p.slope(Point(15,25)))
#
#

#
# # 4.
# # Write a class called Line that represents a line segment between two Points. The following
# # codes is the first version of the Line class
# # class Line:
# # def __int__(self,newp1,newp2):
# # self.p1=newp1
# # self.p2=newp2
# # Then add the following methods to Your Line object:
# # def getP1(self):
# # Returns this Line’s first endpoint.
# # def getP2(self):
# # Return this Line’s second endpoint.
# # def getSlope(self):
# # Return the slope of this Line. The slope of a line between point (x1,y1) and (x2,y2) is equal to
# # (y2-y1)/(x2-x1).
# # def getLength(self):
# # Return the length of this Line.
# # Develop a client program to test your Line class.
#
#
# class Line:
#     def __init__(self, p1, p2):
#         self.p1 = p1
#         self.p2 = p2
#
#     def get_p1(self):
#         return self.p1
#
#     def get_p2(self):
#         return self.p2
#
#     def slope(self):
#         return (self.p2.y - self.p1.y)/(self.p2.x - self.p1.x)
#
#     def getLength(self):
#         return math.sqrt(((self.p2.x - self.p1.x)**2) + ((self.p2.y - self.p1.y)**2))
#
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# line = Line(Point(5,10), Point(30,40))
# print(line.slope())
# print(line.getLength())




# 5. The diagram below represents the design for the BankAccount class
# Class: BankAccount
# accountNumber:String
# accountName:String
# balance:float
# __init__(String, String, float)
# getAccountNumber():String
# getAccountName():String
# getBalance():float
# deposit(float)
# withdraw(float): boolean
# Detailed methods description:
# __init__(String, String,float) is a constructor
# getAccountNumber():String returns the account number
# getAccountName():String returns the account name
# getBalance():float returns the balance
# deposit(float)accepts an item of type float and adds it to the balance
# withdraw(float): Boolean accepts an item of type float and checks if there are
# sufficient funds to make a withdrawal. If there are not, then the method terminates and
# returns a value of false. If there are sufficient funds, however, the method subtracts the
# amount from the balance and returns a value of true.
# Write the code for the BankAccount class.
# Write client code to test out your BankAccount class; it should create two or three accounts,
# and use the methods of the BankAccount class to test whether they work according to the
# specification.
# It is perfectly possible, and often very desirable, to create lists of objects.



class BankAccount:
    def __init__(self, account_number, account_name, balance):
        try:
            account_number = str(account_number)
            account_name = str(account_name)
            balance = float(balance)
        except ValueError as ve:
            print("ValueError", ve)
        self.__account_number = account_number
        self.__account_name = account_name
        self.__balance = balance

    def getAccountNumber(self):
        return self.__account_number

    def getAccountName(self):
        return self.__account_name

    def getBalance(self):
        return self.__balance

    def details(self):
        print("Account Number:", self.__account_number)
        print("Account Name", self.__account_name)
        print("Balance", self.__balance)

    def deposit(self, amount):
        try:
            amount = float(amount)
        except ValueError as ve:
            print("ValueError", ve)
        self.__balance = self.__balance + amount

    def withdraw(self, amount):
        try:
            amount = float(amount)
        except ValueError as ve:
            print("ValueError", ve)
        self.__balance = self.__balance - amount


ba = BankAccount("123", "asif", 500)
ba.details()
ba.deposit(200)
ba.details()
ba.withdraw(100)
ba.details()