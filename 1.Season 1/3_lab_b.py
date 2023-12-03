from math import *
import random

# # 1. Write a program to produce the following output using for loop
# # +----+
# # \ /
# # / \
# # \ /
# # / \
# # \ /
# # / \
# # +----+
#
# for i in range(1, 9):
#     if i == 1 or i == 8:
#         print("+----+")
#     elif i % 2 == 0:
#         print("\\\t/")
#     else:
#         print("/\t\\")
import math


# # 2. Write a program to produce the following output using for loop
# # **********
# # **********
# # **********
# # **********
# # **********
#
# for i in range(0, 5):
#     for j in range(0, 10):
#         if j != 9:
#             print("* ", end='')
#         else:
#             print("*", end='')
#     print("\n")
# 1 line solution
# print(("*"*10 + "\n")*5)


# # 3. Complete the code for the following for loop:
# # 3.a
# for i in range(1,7):
#     print(i)

# # 3.b
# for i in range(1,7):
#     print(i*2)

# # 3.c
# base = 4
# for i in range(1,7):
#     print(base)
#     base += 15

# # 3.d
# base = 30
# for i in range(1,7):
#     print(base)
#     base -= 10

# # 3.e
# base = -7
# for i in range(1,7):
#     print(base)
#     base += 4

# # 3.f
# base = 97
# for i in range(1,7):
#     print(base)
#     base -= 3

# # 3.g
# base = -4
# for i in range(1,7):
#     print(base)
#     base += 18


# # 4. Write a program to produce the following output using for loops. Then
# # use a class constant to make it possible to change the number of lines in
# # the figure.
# # 1
# # 22
# # 333
# # 4444
# # 55555
# # 666666
# # 7777777
# x=7
# for i in range(1, x+1):
#     for j in range(1, i+1):
#         print(i, end='')
#     print("")


# # 5. Write a method named pay that accepts two parameters: a real number
# # for a TA's salary, and an integer for the number of hours the TA worked
# # this week. The method should return how much money to pay the TA.
# def pay(rate, hours):
#     if hours <= 8:
#         return rate * hours
#     return (8 * rate) + (hours - 8) * rate * 1.5
#
# print(pay(4.00, 11))

# 6. Consider the following method for converting milliseconds into days:
# // converts milliseconds to days
# def toDays(millis):
# return millis / 1000.0 / 60.0 / 60.0 / 24.0
# Write a similar method named area that takes as a parameter the radius of
# a circle and that returns the area of the circle. For example, the call

# def area(radius):
#     return 2* math.pi*radius
# print(area(2))


# # 7. Copy and paste the following code into pythons IDLE script
# # environment.
# # low = 1
# # high = 1001
# # sum = 0
# # for i in range(low,high):
# # sum += i
# # print("sum = " , sum)
# # Modify the code to use a input to prompt the user for the values of low
# # and high. Below is a sample execution in which the user asks for the same
# # values as in the original program (1 through 1000):
# # low? 1
# # high? 1001
# # sum = 500500
# # Below is an execution with different values for low and high:
# # low? 300
# # high? 5298
# # sum = 13986903
# # You should exactly reproduce this format.
#
# low = int(input("Enter low value:"))
# high = int(input("Enter high value"))
# sum = 0
# for i in range(low,high):
#     sum += i
# print("sum = " , sum)


# # 8. Write a program using while loop that prompts the user for numbers until
# # the user types 0, then outputs their sum.
# # sum = 0
# x = int(input("Please enter:"))
# while x != 0 :
#     sum += x;
#     x = int(input("Please enter:"))
# print(sum)
#
# sum2=0
# while True:
#     x2 = int(input("Please enter:"))
#     if x2 != 0:
#         sum2 += x2
#     else:
#         break;
# print(sum2)


# # 9. Write a program using while loop that prompts the user for numbers until
# # the user types -1, then outputs their sum.
# # sum = 0
# x = int(input("Please enter:"))
# while x != -1 :
#     sum += x;
#     x = int(input("Please enter:"))
# print(sum)
#
# sum2=0
# while True:
#     x2 = int(input("Please enter:"))
#     if x2 != -1:
#         sum2 += x2
#     else:
#         break;
# print(sum2)


# # 10. Write a method named repl that accepts a String and a number of
# # repetitions as parameters and returns the String concatenated that many
# # times. For example, the call repl("hello", 3) returns "hellohellohello".
# # If the number of repetitions is 0 or less, an empty string is returned.
#
# def repl(str, rep):
#     if rep < 1:
#         return ""
#     ret = ""
#     while rep > 0:
#         ret += str
#         rep -=1
#     return ret
#
# print(repl("hello", 3))

# # 11. Write a method called printRange that accepts two integers as arguments and
# # prints the sequence of numbers between the two arguments, separated by
# # spaces. Print an increasing sequence if the first argument is smaller than
# # the second; otherwise, print a decreasing sequence. If the two numbers
# # are the same, that number should be printed by itself. Here are some
# # sample calls to printRange:
#
# def printRange(start, end):
#     direction = 1 if start<end else -1
#     end = end+1 if start<end else end-1
#     for x in range(start, end, direction):
#         print(x, " ", end='')
# printRange(19,19)



# # 12. Write a method named smallestLargest that asks the user to enter numbers,
# # then prints the smallest and largest of all the numbers typed in by the
# # user. You may assume the user enters a valid number greater than 0 for
# # the number of numbers to read. Here is an example dialogue:
#
# x = int(input("How many numbers do you want to enter?"))
# mini  = maxi = int(input("Number 1:"))
# for i in range(2, x+1):
#     new_inp = int(input("Number "+ str(i)+ ":"))
#     mini = min(mini, new_inp)
#     maxi = max(maxi, new_inp)
# print("Smallest:", mini)
# print("Largest:", maxi)


# # 13. Write a method called printAverage that uses a sentinel loop to
# # repeatedly prompt the user for numbers. Once the user types any number
# # less than zero, the method should display the average of all nonnegative
# # numbers typed. Display the average as a double. Here is a sample
# # dialogue with the user:
#
# def printAverage():
#     total = 0
#     count = 0
#     while True:
#         x = int(input("Type a number:"))
#         if x < 0:
#             break
#         total += x
#         count +=1
#     avg = 0 if count == 0 else total/count
#     print("Average was", avg)
# printAverage()


# # 14. Write a method named numUnique that takes three integers as parameters
# # and returns the number of unique integers among the three. For example,
# # the call numUnique(18, 3, 4) should return 3 because the parameters
# # have three different values. By contrast, the call numUnique(6, 7, 6)
# # should return 2 because there are only two unique numbers among the
# # three parameters: 6 and 7.
#
# def numUnique(n1, n2, n3):
#     if n1 != n2 and n1!= n3 and n2 != n3:
#         print(3)
#         return
#     if n1 == n2 and n1 == n3:
#         print(1)
#         return
#     print(2)
# numUnique(2,2,3)

# # 15. A Random object generates pseudo-random numbers. Find out how to
# # use the Random class and write a program that simulates rolling of two 6-
# # sided dice until their combined result comes up as 7. One possible output
# # can be seen as below:
# def dice():
#     return random.randrange(1,7)
#
# def play():
#     count = 0
#     while True:
#         d1 = dice()
#         d2 = dice()
#         count +=1
#         print(count, ": " ,d1, " + ", d2, " = ", d1+d2)
#         if d1+d2==7:
#             print("You won after ", count ," tries!")
#             break
# play()

