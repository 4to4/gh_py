from pprint import pprint as pp
from math import factorial
from dumper import dump, dumps

# list comparesion 
words = "do I really have it?".split()
lst = [len(word) for word in words]
print(lst)

# this is equivalent to 1. create a list, 2. append length of each word to the list

# another example
f = [ len(str(factorial(x))) for x in range(20) ]
print("GGGGGGGGGGGGGGGG", f)


print(','.join(str(i) for i in ([1,2,3,4,5,6,7,])))

# swapping example
num_to_alpha = dict(a=1, b=2, c=3)
print(num_to_alpha)
alpha_to_num = {num: alpha for alpha, num in num_to_alpha.items()}
print(alpha_to_num)
#swaping

for word in ("followed by a newlin at the end of the".split()):
    print(f"Word {word}")

#sets context
print ({ factorial(x) for x in range(10) })

# dict context
# Double each value in the dictionary
dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
double_dict1 = {k:v*2 for (k,v) in dict1.items()}
print(dump(double_dict1))
print(dumps(double_dict1))

print ([ x for x in range(10) if x % 2 ])
