import copy

tpl = ("we", 4, [2,3,4])
print(tpl)

tup = 2, 3
print(tup)

print(tpl[1])
print(len(tpl))

tpl2 = [5,6,7]
tpl = tpl + tuple(tpl2)

for evr in tpl:
    print("T: ", evr)

print(tpl*2)

print([2,3,4] in tpl)

print(len(tpl))

lst = [1, "two", 3.0]
lst[1] = 2
lst[2] = 3
print(lst)

lst.append(4)
print(lst)
lst.extend([5,6])
print(lst)
v = lst.pop()
print(v)
print(lst)

lst.insert(2, "three")
print(lst)

lst.remove("three")
print(lst)
lst[1], lst[2] = lst[2], lst[1]
print(lst)

lst.sort()
print(lst)

lst.reverse()
print(lst)
lst.reverse()

lst2 = lst
lst.append(6)
print(lst2)

lst3 = lst[:]
lst.append(7)
print(lst)
print(lst3)

lst4 = copy.deepcopy(lst)
lst.append(8)
print(lst)
print(lst4)

lst4 = [x for x in range(10, 16)]
print(lst4)
s1 = "kdjfkjd"
lst4 = [x*3 for x in s1]*2
print(lst4)

lst4 = [x+y for x in range(1,6) for y in range(11, 16)]
print(lst4)

lst4 = [c for c in "Hello There" if c.isupper()]
print(lst4)

tp = (1, "two", 3)
tmp = list(tp)
tmp[1] = 2
tp = tuple(tmp)
print(tp)






