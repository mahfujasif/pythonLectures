from datetime import datetime

with open("../files/nest/nested.txt", 'w') as ff:
    content = "current date is " + str(datetime.now()) + "\n"
    ff.write(content)

with open("../files/nest/nested.txt", 'a') as ff:
    content = "current date is " + str(datetime.now()) + "\n"
    ff.write(content)

with open("../files/nest/nested.txt", 'r') as ff:
    for line in ff:
        print(line, end='')

with open("../files/nest/nested.txt", 'r') as ff:
    print(ff.read(5))
    print(ff.read(5))
    print(ff.read(5))


print("-----------------------------------")
with open("../files/nest/nested.txt", 'r') as ff:
    print(ff.readline(5))
    print(ff.readline(5))
    print(ff.readline(5))


print("-----------------------------------")
with open("../files/nest/nested.txt", 'r') as ff:
    print(ff.readline())
    print(ff.readline())


with open("../files/nest/nested.txt", 'r') as ff:
    l = ff.readlines()
    print(l)
    for index, line in enumerate(l, 1):
        print(index, line, end='')


with open("../files/nest/nested2.txt", 'w') as ff:
    print("Hi there", file=ff)
    print("How you doing", file=ff)
    print("Hey mate", file=ff)


with open("../files/nest/nested2.txt", 'w') as ff:
    ff.write("Hi ")
    ff.write("there")


with open("../files/nest/nested2.txt", 'w') as ff:
    ff.writelines(["Hi there\n", "Whats up"])



