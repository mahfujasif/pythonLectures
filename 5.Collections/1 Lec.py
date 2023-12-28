
line = "-".ljust(50,"-")
contacts = {'asif': 123, 'mahfuj': 456}
print(contacts)

dc = {(1,2): 'one two', '34': 3}
print(dc)

print(dc[(1,2)])

dc['new'] = 3.2
print(dc)

dc['new'] = 'jj'
print(dc)

print('new' in dc)

dc.clear()
print(dc)

my_dc = {1: "oneee", 2:"three"}
ur_dc = {2: "two", 1:"one"}
my_dc.update(ur_dc)
print(my_dc)
print(ur_dc)

new_dc = my_dc.copy()
print(my_dc)
print(new_dc)
new_dc[3] = "three"
print(my_dc)
print(new_dc)

v = new_dc.pop(3)
print(new_dc)
print(v)

for itm in my_dc.items():
    print(itm)
for keys in my_dc.keys():
    print(keys)
for vals in my_dc.values():
    print(vals)

print(my_dc.get(10, "oneeee"))



words = """Imagine you are trying to count the frequency of word
occurrence in a list of words (perhaps gathered from a
text file). We can represent those data using a
dictionary, with the words as the keys and the values
as the frequency of occurrence. There are two
operations you need to perform in the process of
updating a dictionary with a word from the list"""
words = words.replace(")", "")
words = words.replace("(", "")
words = words.replace(".", "")
words = words.replace("\n", " ")

word_count = dict()
word_list = words.split(" ")
for word in word_list:
    tmp_c = word_count.get(word, 0)
    tmp_c = tmp_c + 1
    word_count[word] = tmp_c
print(line)
for itm in word_count.items():
    print(itm[0] + ":" + str(itm[1]))
print(line)

st1 = {1,2,2, "ddf"}
st2 = {1,3}

print(st1)
print("ddf" in  st1)

st3 = st1.intersection(st2)
st3 = st1 & st2
print(st3)

st3 = st1 - st2
st3 = st1.difference(st2)
print(st3)

st3 = st1 | st2
st3 = st1.union(st2)
print(st3)

st3 = st1 ^ st2
st3 = st1.symmetric_difference(st2)
print(st3)

print(st1 > st2)


st1.discard("ffgf")

print(st1.symmetric_difference(st2))

print(line)
v = zip("abc", [1,2])
print(list(v))

v = dict(zip("abc", [1,2]))
print(v)

dc = {1:1, 2:2}
for k,v in dc.items():
    print(k, " : ", v)

ls = ["one", "two", "three"]
for i,v in enumerate(ls, 5):
    print(i, " - ", v)



a_dict = {k:v for k,v in enumerate('abcdefhg')}
print(a_dict)

b_dict = {v:k for k,v in a_dict.items()}
print(b_dict)

b_list = [(k,v) for k, v in b_dict.items()]
print(b_list)

r_dict = {0:'a', 2:'c', 1:'b'}
print(r_dict)

sorted_dict = {k:r_dict[k] for k in sorted(r_dict)}
print(sorted_dict)

r_list = [(k,v) for k,v in r_dict.items()]
r_list = sorted(r_list)
print(r_list)
sorted_dict2 = {t[0]:t[1] for t in r_list}
print(sorted_dict2)

char_set = {ch for ch in "this is text"}
char_set = sorted(char_set)
print(char_set)