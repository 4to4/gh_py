import math
from pprint import pprint as pp
# tuples - immutable sequence of objects
# range - arthemetic progression of integers
# set - mutable collection of unique immutable objects

# tuples

tup = ('<', 9, 4)
print(tup)
print(len(tup))

for item in tup:
    print(item)

#single element tuple
tup2 = (23,) # the comma is needed to tell python that tuple and not a function call to int
print(tup2)

#empty tuples
tup3 = ()
print(tup3)

def minmax(i):
	return min(i),max(i)

h, x = minmax([1,2,3])
print(h,x)

#join
print(';'.join(['h', 'fd', '1', '4', '5']))
tup4 = 'h', 'fd', '1', '4', '5'
print(';'.join(tup4))

print(''.join(['h', 'fd', '1', '4', '5']))

print("ritesh".partition('i') )

print("This is {} of the names of {} grams {}".format('one', 'two', 'three'))

print("T x={pos[0]} y={pos[1]}".format(pos=(1, 'two')))

print("Pi is {m.pi}, e={m.e}".format(m=math))

print("Pi is {m.pi:.3f}, e={m.e:.4f}".format(m=math))
print(f"Pi is {math.pi}")
print(f"Pi is {math.pi:0.3f}")

#range
# print('-'.join(range(0,5)))

print(', '.join(str(x) for x in range(0,5)))
# print(', '.join(str(i) for i in range(0,4,2)))

t2 = (1,3,4,5,6,7)
for i,v in enumerate(t2):
    print(f"index={i} value={v}")

r = [1,2,3,4,4,5,5]
print(r[-4])
print(r[1:3])
print(r[1:-1]) # first and last index

# copying copies only reference of the object #SHALLOW COPY
# e.g. 
r = [1,2,3,3,4,4]
s = r[:] # return all the elements from 0th element and copy them to s. But that copy will be only reference copy. 
print (r is s) #but
print (r == s) # the correct way to do it is
s = r.copy() 
s = list(r)
print(s)

c = [ 1,2]
d = c * 3
print(d)

a=['0'] * 5
print(a)
a[2] = 5
print(a)

h = 'y Robert Smallshire, and Austin Bingham'.split()
print(h)
h.sort(key=len)
print(h)

#dict
d1 = { 'a': 1, 'b': 2 }
print(d1['a'])

#dict constructor
alist = ['aa','2a','3a','4a' ]
d2 = dict(alist) # or d2 = dict(['aa','2a','3a','4a' ])
print(d2)
# OR
ph = dict(a=1, b=2, c=3, d=5)
print(ph)

for k in ph.keys():
    print(f"key => {k}")

for k,v in ph.items():
    print(f"key => {k} values =>{v}")

for value in ph.values():
    print(f"values => {value}")

print('a' in ph) # checks only keys
print('1' in ph)

pp(ph)

#sets
set1 = set("Core Python: Getting Getting Getting Getting Getting Getting Started".split())
print(set1)

