# # 1 Given the string "Monty Python":
# s = "Monty Python"
# # (a) Write an expression to print the first character.
# print(s[0])
# # (b) Write an expression to print the last character.
# print(s[-1])
# # (c) Write an expression including len to print the last character.
# print(s[len(s)-1])
# # (d) Write an expression that prints "Monty".
# print(s[:5])


# # 2. Given the string "homebody":
# # (a) Write an expression using slicing to print "home".
# s = "homebody"
# print(s[:4])
# # (b) Write an expression using slicing to print "body".
# print(s[4:])

#
# # 3. Given a variable S containing a string of even length:
# s = "123456"
#
# # (a) Write an expression to print out the first half of the string.
# l = len(s)//2
# print(s[:l])
#
# # (b) Write an expression to print out the second half of the string.
# l = len(s)//2
# print(s[l:])

# # 4. Given a variable S containing a string of odd length:
# s = "1234567"
#
# # (a) Write an expression to print the middle character.
# print(s[len(s)//2])
#
# # (b) Write an expression to print the string up to but not including the middle character (i.e., the first half of the string).
# print(s[:len(s)//2])
#
# # (c) Write an expression to print the string from the middle character to the end (not
# # including the middle character).
# print(s[(len(s)//2)+1:])


# # 5. Given x = ‘water’, what is returned by x.replace('w','c',1)?
# # 'cater'
# print("water".replace('w', 'c', 1))

#
# # 6. Given the string S = "What is your name?":
# # (a) What is returned by S[::2]?
# 'Wa syu ae'
# S = "What is your name?"
# print(S[::2])
#
# # (b) What is returned by S[2:8:-1]?
# # ''
# print(S[2:8:-1])


# # 7. Given the string variable x = 'acegikmoqsuwy' and y = '+bdfhjlnprtvxz',
# # use indexing to create a string z that is the lowercase English alphabet.
# x = 'acegikmoqsuwy'
# y = '+bdfhjlnprtvxz'
# i = 0
# z = ''
# while i < 13:
#     z += x[i]
#     z += y[i+1]
#     i+=1
# print(z)


# 8. The plus sign (+) is overloaded in Python. Explain why 5 + 4 equals 9, '5' + '4'
# equals '54', and 5 + 4.0 equals 9.0.
# 'Overloading method's behaviour is determined by the argument type'

# # 9. What will be printed by the following?
# # 'This is a test.This is a test.This is a test.'
# x = 'This is a test.'
# print(x * 3)


# # 10. In the following program, replace the for with a while loop.
# # S="I had a cat named amanda when I was little"
# # count = 0
# # for i in S:
# #     if i == "a":
# #         count += 1
# # print(count)
#
# count = 0
# i = 0
# while i < len(S):
#     if S[i] == "a":
#         count += 1
#     i += 1
# print(count)


# # 11. (String operators) The Monty Python comedy troupe has a famous skit set in a
# # restaurant whose menu is predominately Spam—a canned meat mixture of ham and pork.
# # One menu entry was “Spam, Spam, Spam, Spam, Spam, baked beans, Spam, Spam, Spam,
# # and Spam.” Write a Python string expression using both the concatenation (+) and
# # repetition (*) string operators to form that menu entry.
# print("Spam, Spam, Spam, Spam, Spam, baked beans, Spam, Spam, Spam, and Spam.")
# print("Spam, "*5 + "baked beans, " + "Spam, "*3 + "and Spam.")


# # 12. The following Python statement generates this error: “ValueError: too many values
# # to unpack.” Why?
# # first,second = input('two space-separated numbers:')
# first,second = input('two space-separated numbers:').split(" ")



# # 13. We know that writing the following code:
# #   print("I like writing in Python.")
# #   print("It is so much fun.")
# # will result in:
# #   I like writing in Python.
# #   It is so much fun.
# # when executed. However, can you manage to do this same task with only one line of
# # code?
# print("I like writing in Python.\nIt is so much fun.")


# # 14. Five string methods manipulate case: capitalize, title, swapcase, upper,
# # and lower. Consider the strings: s1 = "concord", s2 = "souix city", s3 =
# # "HONOLULU", and s4 = "TopHat".
# s1 = "concord"
# s2 = "souix city"
# s3 = "HONOLULU"
# s4 = "TopHat"
# # (a) Describe what capitalize does.
# print(s2.capitalize())
#
# # (b) Describe what swapcase does.
# print(s4.swapcase())
#
# # (c) Describe what upper does.
# print(s1.upper())
#
# # (d) Describe what lower does.
# print(s3.lower())
#
# # (e) Describe what title does.
# print(s2.title())


# # 15. It is possible to combine string methods in one expression. Given the expression
# # s="CAT", what is s.upper().lower() ?
# # 'cat'
# print("CAT".upper().lower())

# # 16. Two string methods left and right justify strings within a specified width. In
# # addition, they default by filling in with spaces but can be specified to fill in with
# # a character. Consider s = "Topkapi" and s.rjust(20,".") or s.ljust(15). Experiment
# # with right and left justification. Describe the rules for what ljust and rjust do.
# print("Topkapi".rjust(20,"."))
# print("Topkapi".ljust(15))

# # 17. Two string methods find where a character is in a string: find and index.
# # (a) Both work the same if a character is found, but they behave differently if the
# # character is not found. Describe the difference in how they behave when the
# # character is not found.
# print("abc def".find("xx"))
# print("abc def".index("xx"))

# # (b) The find and index methods are not limited to finding single characters. They
# # can search for substrings. Given s = "Topkapi", what does s.find("kap")
# # print? Describe the rule for what find prints.
# # ans: prints 3
# print("Topkapi".find("kap"))

# # 18. Using the input command, prompt for input and then convert the input to lowercase.
# print(input("Enter something in uppercase:").lower())

# # 19. Convert a string that is all capitals into a string where only the first letters
# # are capitals. For example, convert "NEW YORK" to "New York".
# s = "NEW YORK"
# print(s.title())

# # 20. Experiment with the count method. What does it count?
# # For example,
# #   some string = "Hello world!"
# #   some string.count("o")
# s = "Hello world!"
# print(s.count("o"))

# # 21. Experiment with the strip method. What does it do?
# # For example,
# #   some string = "Hi!......"
# #   some string.strip(".!")
# s = "Hi!......"
# print(s.strip(".!"))

# 22. The string methods that start with “is” all return either True or False.
# Experiment with them to figure out how they work—i.e., what causes them to return
# “True” and what causes them to return “False.”


# # 23. Let, name str = 'Albert Einstein'. How would you extract the first name
# # and last name from name str using string operator ‘:’?
# s = 'Albert Einstein'
# l = s.find(" ")
# first = s[:l]
# sec = s[l+1:]
# print(first)
# print(sec)

# # 24. In British English, there is the word flavour. The American spelling is “flavor”.
# # Suppose you have a string in Python called brit word = 'flavour' and you want to
# # convert it into the American variant and store it in a string called amer word. How
# # would you do it?
# brit_word = 'flavour'
# amer_word = brit_word.replace('u', '')
# print(amer_word)

# # 25. Which of the following works without any error?
# # (a) var = 'xyz' * 10.5
# # (b) var = 'xyz' * '5'
# # (c) var = 'xyz' * 5
# # (d) var = 'xyz' * 5.0
#
# # ans: c
# print('xyz' * 5)


# # 26. (Reversing a string) Given a string variable X = 'Alan Turing', write an
# # expression to reverse it to get string Y = 'gniruT nalA'.
# x = 'Alan Turing'
# print(x[5::-1])

# # 27. Suppose you have a string ab string = 'abababababababab'. Write an
# # expression to remove all the b’s and create a string a_string = 'aaaaaaaa'.
# ab_string = 'abababababababab'
# a_string = ab_string.replace('b', '')
# print(a_string)


# # 28. Given the string 'abcdefghij', write a single line of code that will print the
# # following (Hint: Slicing is your friend):
# s = 'abcdefghij'
# # (a) 'jihgfedcba'
# print(s[::-1])
# # (b) 'adgj'
# print(s[::3])
# # (c) 'igeca'
# print(s[-2::-2])

# # 29. Using the find method, write a short program that will print out the index of both
# # o’s when given the input “Who’s on first?”
# s = "Who’s on first?"
# print(s.find('o'))
# print(s.find('o', 3))


# # 30. Write a program that given a name in the form of “Chapman, Graham Arthur” will
# # convert it to the form “Graham Arthur Chapman.”
# s = "Chapman, Graham Arthur"
# sp = s.rsplit(',')
# print("".join(sp)+".")

# # 31. The expression ‘dog’ + ‘s’ will return ‘dogs’. What is returned by the
# # expression ‘dog’− ‘g’ ? Explain.
# # ans: unsupported operator type
# print('dog'-'g')





