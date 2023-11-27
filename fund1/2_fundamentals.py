from math import *


# print(1+4*3)

# print(10**33)

# print(100-90+10*3/6%3**2)

# print(7 / 3 * 1.2 + 3 / 2)

# print(15/4)
# print(15//4)
# print(52//27)


# print(abs(-5.6))
# print(ceil(5.6))
# print(ceil(-5.6))

# print(floor(5.6))
# print(floor(-5.6))

# print(cos(2*pi))

# print(e**3)
# print(log(20))

# print(log10(100))

# print(max(e,pi))
# print(min(e,pi))

# print(round(5.50000001))

# print(sin(.5*pi))
# print(tan(.6*pi))

# print(sqrt(36.2))

# x=5
# print("x+2 is", x+2)


# age = int(input("Enter a number: "))
# print("Your input is", age)

# for x in range(1, 6):
#     print(x)
#
# for x in range(1, 10, 2):
#     print(x)

# for x in range(2, -10, 5):
#     print(x)

# for x in range(1, 2, 10):
#     print(x)

# sumV = 0
# for i in range(1, 11):
#     sumV = sumV + (i * i)
#
# print("Sum of first 10 number square is : ", sumV)
#
#
# # factorial finder
#
#
# while True:
#     inp = int(input("Enter a number: "))
#     fac = 1
#     for i in range(1, inp + 1):
#         fac *= i
#     print("Factorial is: ", fac)


# gpa = .4
# if gpa > 3:
#     print("noice")
# elif gpa > 2:
#     print("noicee")
# else:
#     print("noiceeee")
#
# num = 1
# while num < 10:
#     print(num)
#     num = num*2

# class Mc:
#     x = 5
# class Yc:
#     x = 5
# p1 = Mc()
# p2 = Mc()
# p3 = Yc()
# print(p1 == p2)
# print(p1 == p3)
# p2 = p1
# print(p1 == p2)
# p2.x=3
# print(p1.x)
# print(p1 == p2)


# print(3>2 and 5>4)
# print(1<2 or 2<1)
# print(not(2<1 and 1<2))

# x = "hello, can you provide \"MOP\" to me?"
# print(x)
# x="hello\nhow are you?\nIm good,u?"
# print(x)
# x="0123"
# print(x[0])

# x = "Hello, how can i help you?"
# print(len(x))
# print(x.lower())
# print(x.upper())
# print(x)

# x = input("input please:")
# print("input is:", x)

# x = "2345"
# for d in x:
#     print("each", d)

# print(ord("A"), ord("Z"), ord("a"), ord("z"), ord("0"))
# print(chr(65), chr(90), chr(97), chr(122), chr(48))

# Exercise: Write a program that performs a rotation cypher.
# – e.g. "Attack" when rotated by 1 becomes "buubdl"

# inp="Attack"
# outp = ""
# for i in inp:
#     outp += chr(ord(i) + 1)
# print(outp)


# File process
# inp = open("files/hello.txt").read();
# print(inp)

# for lines in open("files/hello.txt").readlines():
#     print(lines)

# count = 0
# for lines in open("files/hello.txt").readlines():
#     count = count+1;
# print(count, " lines found")

# c_c=0
# c_g=0
# c_t=0
# seq = open("files/DNA").read()
# for protein in seq:
#     c_t += 1
#     if protein == 'C':
#         c_c += 1
#     elif protein == 'G':
#         c_g += 1
# print("total C:", c_c)
# print("total G:",c_g)
# print("total:", c_t)
# c_plus_g = c_c+c_g
# percent = (c_plus_g/c_t)*100
# print("Percentage is ", percent)

# Function call
# def drawbox(arg):
#     print("Received:", arg)
#     print("+---+")
#     print("|   |")
#     print("|   |")
#     print("+---+")
#
#
# print("Calling func")
# drawbox(100)

