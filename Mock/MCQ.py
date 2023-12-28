import math
# # 1
# print("\'datascience\'")

# # 2
# 'datascience'.[4:]

# # 3
# print("dff" + "dff")

# # 4 ans none
# S = 's,pa,m'
# print(S[2:3])
# print(S[2])

# # 5
# S = 'Big Data 2022'
# print(S.lower())

# # 7
# S = 'data science'
# print(S.find('e'))

# T1 = (1, 2, 4, 3)
# T2 = (1, 2, 3, 4)
# print(T1>T2)

# D ={1:'a',2:'b',3:'d'}
# print(D)

# print({0, 0, 'a', 0, 9})

# set1={'a', 'b'}
# set2={'c', 'd'}
# print(set1|set2)

# set1 = {'a', 'b', 'c', 'd'}
# set1.add('a')
# print(set1)

# print(set('aabbccdd'))

# print(abs(math.sqrt(36)))

# print(4 < 5  > 7)

# print(chr(ord('A')))

# print(id(1))

# L=[5,2,3,1,4]
# L.reverse()
# print(L)

# x=1
# y=0
# print(x>=2 and (x/y)>2)

# L=[2,4,1,7,3,4,2,1,5,7,3,1]
# p = list(set(sorted(L)))
# print(p)

# L = [1,2,-3,2,-1,4,-2,8]
# p = [x for x in L if x>0]
# print(p)

# D1 = {'a':1, 'b':2, 'c':3}
# D2={'d':3, 'e':5}
# D1.update(D2)
# print(D1)


x= 1

# while True:
#     if x % 2 == 0:
#         break
#     print(x)
#     x += 1

# i= 0
# while i <3:
#     print(i)
#     i += 1
# else:
#     print(0)


L1 = [2, 3, [4, 5]]
L2 = L1.copy()
L2[2][0] = 100
print(L1, L2)