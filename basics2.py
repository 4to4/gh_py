import sys
# constructors like list(), dict() set(), tuple() converts the given data set into tuples


string = "A feature transformer might take a DataFrame, read a column"
lst = list(string)
print("List ", lst)

tp = tuple(string)
print("Dict ", tp)

st = set(string)
print("Set", st)

# prints the name of the package / module
print(__name__)


# if a module should be imported at same time should also be executable then use following if for that.
# here the function will have the contents of the package
def func():
    """ This is doc string """
    pass

if( __name__ == '__main__'):
    func()

# to get the doc string of a function
print(func.__doc__)

# function id shows the object address
print(id(string))

# is operator is used to compare two objects if they are equal
if ( string is string):
    print("Same objects")



### scoping
# local or enclosing are scoped inside a function
# global = global to the whole program
# built-in is like @INC

#prints type of object
print(type(string))
print(type (tuple(([1,1,2,2,3,4,5,5]))))

#prints module attributes available for a given module
print(dir())

#tuple unpacking - like returning list in perl
def minmax(a,b):
    return a, b

print(minmax(1,2))

# perl join is join
print(':'.join(list("ritesh")))

# perl split is split
print("R it e s h".split())

#partion function # this is like string tockeniser
print("thisisgoingtohappen".partition('going'))

for i in (list("ritesh")):
    print(f"i -> {i}")

#enumerator returns index and the value of the iteratee
print(dict(enumerate(list("where is the".split()))))

#copying
a = list("str1")
b = list("str2")
c=a # this copy only makes the reference copy called shallow copy
print(id(a), id(c)) #

#to make proper copy, use copy function, works for list
x = a.copy()
print(x)

# perl like x function. Here x is *
st = [1,2]
print (st * 4)

# creating dictionaries dynamically
my_dict = (
    dict(
        enumerate
            (
                list(
                    "Processing large volumes of data using Data Frames HIVE tables and ETL in".split()
                    )
            )
        )
    )


# sort vs sorted:
# sort sorts the list inplace and hence changes it, it's method invoked with .
# sorted create a sorted list but makes a new copy of the list, it's a function
# you cannot use sort on a dict keys because sorts things inplace


#printing dict with sorted keys numeric
dict2 = {4:  34, 12: 34, 5: 23434, 1: 65765, 654645: 1}
for i in sorted(dict2.keys(), key=int): # this will sort the list numerically
    print(f"K:{i}  V:{dict2[i]}")

for i in sorted(dict2.keys(), key=str): # this sorts in string context
    print(f"K2:{i}  V2:{dict2[i]}") 

for i in sorted(dict2.keys(), key=str, reverse=True): # this sorts in string  but reverse
    print(f"K3:{i}  V3:{dict2[i]}") 


# sorting the keys of a dict
print(sorted(my_dict.keys()))

# sorting
lst = list("Processing large volumes of data using Data Frames HIVE tables and ETL in".split())
print(lst) # before
lst.sort(reverse=True)
print(lst)  # sorted reverse true
lst.sort(reverse=False, key=str)
print(lst) # sorted reverse false

# dicts syntax with = sign
dict2 = dict(a=1, b=2) # using a dict constructor with key value equan sign
print(dict2)

#exists check in dict
print('a' in dict2.keys())
# OR
print('a' in dict2) # this will check in keys only


# sets - how to manupulate sets and their functions
set1 = {1,2,2,4}
print(set1.union({11,22,33}))

print(set1.difference((5,6,7,8,8,8,8,8,8)))

print(
    set1.intersection(
        list([11,22,3,4,5,6,7])
        )
    )

print(
    set1.issubset(
        (1,2,2,4,5)
    )
    )

print(
    set1.union( 
        list("abcdefg"))
    )


## __repr__ is internal representation of string, very useful in expcetion handling
some_string = "yo mama"
print(f"st -> {some_string!r}")

#exception handling try, catch, finally and use tracestake with it
#there is no catch in python
def dev_zero():
    a = 0
    try:
        a = a/0
    except (ZeroDivisionError, ConnectionAbortedError) as e: # here more than one exception can be added
        print(e.__repr__) # this is called repr
        print(e.__str__) # this is string representation of the repr
        print("Cannot divide by zero", e.__str__) # custom message with error string
        print(f"Full Error is {e!r}") #short to print repr for exception object
        raise e # raising the exception. This is optional.
    else: # you can put as many elses here
        print(f" ----> Exception is raised")

dev_zero()

