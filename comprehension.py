# Comprehension is return context of perl map function.
# Comprehension = map function in perl 

# List Comprehensions
# Dictionary Comprehensions
# Set Comprehensions
# Generator Comprehensions


words = "its about to happen be be be prepared".split()
lst = [len(word) for word in words]
print("List  comprehension", type(lst), lst)
print("-------------------------------------")
# This is list comprehension. Exception the syntax there is no difference between list and generator comprehesions
# Gen comprehension uses () and List uses []
# Gen retrieves values one by one, where as list has all the values in it

gen = (len(word) for word in words)
print("Generator comprehension", type(gen), gen)
for i in gen:
    print(f"Gen comprehension Elements {i}")
print("-------------------------------------")

#Same as list comprehension but only uniques
set = {len(word) for word in words}
print("Set   comprehension", type(set), set)
print("-------------------------------------")

#Same as List comprehension but since tuples and lists are same explicit constructor is needed to denote the tuple
tup = tuple(len(word) for word in words)
print("Tuple comprehension", type(tup), tup)
print("-------------------------------------")

#dictionary comprehension. Notice two variables, notice items function and notice : between the two variables in the curly braces
dict2 = dict(enumerate(list("QWERTY"))) # creating a dict from a string
comp_dict = { x:y for x,y in dict2.items() }
print(comp_dict)

#This can get more complicated as we add expressions to it e.g.
comp_dict = { x:f"{y}" +" PH" for x,y in dict2.items() }
print(comp_dict)

# adding filters to it at the end
comp_dict = { x:f"{y}" +" PH" for x,y in dict2.items() if x % 2}
print(comp_dict)

# handling missing element in a dictionary or KeyError
person = {'name': 'Phill', 'age': 22}
# print(person["d"]) - This will fail and produce keyError

# The solution is use get method on the dict.
# get() takes two arguments get(key, default_value)
# the default_value is optional. If provided the it will returned but only if key is not found.
# get will return None if the key is not found
# default_value if the key is found but default_value (second argument) is specified
# https://www.programiz.com/python-programming/methods/dictionary/get

print(person.get("d", "Unknown")) # This will return Unknown because second argument is specified
print(person.get("name", "Unknown")) # this will return phill since name is a valid key
print(person.get('X')) #This will return None since the key does not exist


print("Nested functions!!!!!")
# Nested functions # not really useful
def ofunc():
    student = ["a", "b"]
    for i in student:
        print(i)
    def ifunc():
        print(student)
    ifunc() # nothing this is being called from outter function. 
   
ofunc()
# this will print 
a
b
from inside ['a', 'b']



# lambda functions
#Anonymous functions, for throw away purposes

#regular functions
def double(x):
    return x * 2

double(2)

#equivalent lambda function
double = lambda x: x * 2
print(type(double))

#format is 
#<function_name_place_holder> = lambda input_argument: function body

# this is very usefule for filter functions
# filter functions are used for filtering
# filter() takes two arguments 1. function 2. list
# filter retuens filter object. so the results must be used with constructor usually list

#generate list of numbers divisible by 3

div3 = lambda x: not (x % 9)
list = list(filter(div3, range(1,100)))
print(list)


# perl map is same as python map function
# and usually together with lambda e.g.
# Unlike perl python returns map object, which has to be converted
# into list or set or some other iterable structure

a_list = [1,2,3,4,5,]
m_list = map( lambda x: x*2, a_list)
# map object to list conversion - must be done
print(list(m_list))

# output will be  => [2, 4, 6, 8, 10]

