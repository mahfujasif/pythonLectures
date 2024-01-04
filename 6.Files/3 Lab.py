# # 1. Write a Python program that will open a file named this.txt and write every other
# # line into the file that.txt
#
# inf = "../files/this.txt"
# ouf = "../files/that.txt"
# with open(inf, 'r') as inf, open(ouf, "w") as ouf:
#     for lines in inf.readlines():
#         ouf.writelines(lines)
# print("done")


# # 2. Create a file words.txt that contains a paragraph of random words (approximately
# # 100 words long). Next, create a program that prompts for the file name then iterates
# # through each word in this file and counts the frequency of each letter (a through z)
# # and stores the values in a dictionary. Make each letter lowercased and ignore
# # punctuation.
#
# filename = input("Please enter file name: ")
# filename = "../files/" + filename + ".txt"
# res = dict()
# with open(filename, 'r') as infile:
#     content = infile.read()
#
# for char in content:
#     char = char.lower()
#     if char.isalpha():
#         count = res.get(char, 0)
#         res[char] = count + 1
# srt = sorted(res)
# for itm in srt:
#     print(itm, " : ", res[itm])


# # 3. Create a test file with a single sentence of 20 words. Read the file, then insert
# # carriage-return characters (\n) and write the test to a new text file that will be
# # composed of four lines of five words.
#
# with open("../files/line in.txt", 'r') as inf, open("../files/line out.txt", 'w') as ouf:
#     content = inf.read()
#     wl = content.split(" ")
#     count = 0
#     line = ''
#     for wrd in wl:
#         line = line + wrd + " "
#         count = count + 1
#         if count == 5:
#             line = line + "\n"
#             ouf.writelines(line)
#             line = ''
#             count = 0
# print("done")




# # 4. Write a program that opens two files: one for reading, the other for writing. The
# # program reads, one line at a time, from the file named input.txt. The line is
# # stripped (to remove the carriage return), and then iterated through, one character at a
# # time. We add each character to the left of a new string called new str, thus reversing
# # the line. After processing the line, we write new str to a file called output.tx
#
# with open("../files/in4.txt", 'r') as inf, open("../files/out4.txt", 'w') as ouf:
#     llist = inf.readlines()
#     for ln in llist:
#         ln = ln.strip()
#         tmp = ""
#         for char in ln:
#             tmp = char + tmp
#         tmp = tmp + "\n"
#         ouf.writelines(tmp)


# # 5. Write a program that prompts for three numbers. Divide the first number by the
# # second number and add that result to the third number. Using exceptions check for the
# # following errors: ValueError, and ZeroDivisionError.
# try:
#     a, b, c = int(input("Enter a numer: ")), int(input("Enter a numer: ")), int(input("Enter a numer: "))
#     print((a / b) + c)
# except ValueError as te:
#     print("Value error: ", te)
# except ZeroDivisionError as ze:
#     print("Value error: ", ze)


# # 6. Write a program using a try-except construct, in the context of user interaction. The
# # goal of the program is to read a line, indicated by a line number, from a file. The user
# # is required to provide both the file name and the line number.
#
# try:
#     fn = input("Enter file name:")
#     fn = "../files/" + fn + ".txt"
#     ln = int(input("Enter line number:"))
#     with open(fn, 'r') as inf:
#         lns = inf.readlines()
#     print(lns[ln - 1])
# except IOError as ie:
#     print("IoError:", ie)
# except ValueError as ve:
#     print("ValueError:", ve)
# except IndexError as ine:
#     print("IndexError:", ine)

