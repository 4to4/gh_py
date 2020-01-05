# gh_py
git hub python

Full practice file:
------------------------------------ start ------------------------------------------------

>>Data types
int
string
boolean
list
dict
set
tuples
frozen sets
complex

>>Python typing:
Java, C, C# - statically typed
e.g. int answer = 20

python - dynamically typed but strongly typed
No type declaration needed but once a type is interpreted by the python compiler then it cannot be changed futher, dynamically or implicitly.
e.g. 

answer = 42 # this will determine the data type of python as int
right after if I try to concatenate a string to it. 
answer = 43 + "FDAFAS" this will throw an error because answer is already typed as int. That is what strongly typed means.

Unlike in perl this code is legal and will work just fine.

$k = 5;
print $k, "\n";
$i = 10;
$j = " Str!\n";
$k = $i . "$j";
print $k, "\n";

>Type hinting:
cannot prevent the code from running...

You can write unit tests to avoid the dynamically typed and dynamically produced errors

>>Comments
""" Comment """ - docstring
# - single line comments


>>strings and formats
my_str = "this is string"
print(f"This string is {my_str}") # string format
print(r"THIS iS A raw sttring!!!!!") # raw string
print("This string is {0}".format(my_str)) # string formatter with sequence number for variables
print("This string is {}".format(my_str)) # since only one string it works the same way

>>Boolean
true_val = True
print(">>" , true_val)

true_val = False
print(">>" , true_val)

>> None Type
None is NULL similar to ther language
This variable was defined but has not value assigned to it.

if (g == None):
    print("Yo")

>>if defined block
a = "String"
if (a):
    print("Yo")

>>ternary operator
a = 1
b = 2
print("bigger") if a > b else print("smaller")

or this works too

a = 1
b = 2
c = "bigger" if a > b else "smaller"
print(c)


>>Lists - Arrays in other languages
lst = ["A", "BAS"]
print(lst)

The index is circular. e.g. -1 index gives you last element

> check if an element is in the list
if ("This" in lst):
    print("This is there.")
#or
print(("This" in lst) == True)

> number of elemets in the list / array
print len(lst)

>other operators in lst can be seen with . operator

>list slicing
print(lst[1:]) # ignore first element and print return till the end
print(lst[1:-1]) # ignore the first and last element in the list

>>loops
>for loop

lst = list(r"PyCharm 2019.3.1 (Community Edition) Build #PC-193.5662.61, built on December 18, 2019".split())
for name in lst:
	print("Name is ", name)

> There is no foreach loop there

> range function produces list
e.g.
for i in range(0,4):
	print ("Range element {0}".format(i))

range function supports 3 arguments => range(5, 10, 2) => start, end, stepping

> break and continue
for i in range(0,20,4):
    print ("Range element {0}".format(i))
    if (i == 8):
        print("found 8 breaking with keyword break")
        break
    else:
        print("No 8 yet, continuing with continue keyword")
        continue

> while loop and auto increment
x = 10
while( x < 13 ):
    print("Count is {0}".format(x))
    x+=1

> there is no ++ or -- in python, instead use += and -=


>> dictionaries - perl hashes

student = {
    "name": 1,
    "student": 12,
    "feedback": 89
}

for k in student.keys():
    print (f"Key {k} -> Value {student[k]}")

for v in student.values():
    print (f"Value {v}")

for k,v in enumerate(student):
    print (f"Key {k, v}")

del student["name"] ############# This deletes the element like perl does
print("Deleted name")

for k,v in enumerate(student):
    print (f"Key {k, v}")

 if an element does not exist then python raises exception

>>exception handling
"""Exceptions """
try:
    print(student["fakeKey"])
except KeyError as e:
    print("This is exception ", traceback.print_exc(file=sys.stdout)) ## << This is generic exception
except Exception:
    print("this is unknown error!")
finally:
    print("this is finally block")

try:
    print(student["fakeKey"])
except KeyError as e:
    print("This is exception ", e.__str__())
    print("this is unknown error!")
finally:
    print("this is finally block")

> notice tracebak module, with sys above for exception handling

>> tuples are lists / arrays which we cannot change values of 
tupl1 = (1, 2,3, 4, '3', 4)
print(tupl1)

>> sets are arrays but unique
st1 = { 1, 3, 4, 5, 5, 5, 5,5, '5' }
print(st1)

>>Function calls 

>named parameters for function calls
def test_func2(i, name, last_name):
    print("this is python!!!!")
    print(f"i {i} name {name} last_name={last_name}")

test_func2(i=10, last_name="RYN", name="Wade") ### names parameters

> optional arguments
def test_func(i, name, last_name='bing'):
    print("this is python!!!!")
    print(f"i {i} name {name} last_name={last_name}")
test_func(10, "RYN", "Wade")

>using *args
def var_args(name, *args):
    print(name)
    print(args)

var_args('THISNAME', 'arg1', 'args2', 'args3', 4, True, None)

The args holds all the arugments but as  a list
The output of the above code is
name
('arg1', 'args2', 'args3', 4, True, None)
Here the name is printed separately and rest of the args are printed as list
To avoid this, use *kwargs, which turns the list into dictionary

>using **kwargs
#using **kwargs
def var_kwargs(name, **kwargs):
    print(name)
    for k in kwargs.keys():
        print(f"{k}->{kwargs[k]}")
    print(kwargs["desc"], kwargs["fb"])

var_kwargs("Yo_name", desc="DEDEDE", fb="Feedback", other="OTHER")

This captures all the arugments in dictionary format

>nested function


>>Yield and generator
def func1():
    for i in range(10):
        print(f" -> {i}")
        yield i
    return

def func2():
    for i in func1():
        print(i)

func2()

Here the yield, stores the process image into the registarts and stack in the cpu when yield is called.
and resumes it when called the next time.

The idea is to iterate through the a data set created by a function but only one by one.
This saves memory and time because it's executing only oe dataset at a time

>>lambda

# Regular function
def twice(i):
    print(i * i)

twice(4)

# corresponding lamda
twotimes = lambda i: i * i

print (twotimes(5))

Lambda is function pointer, so that it can be passed to other functions

>>classes

class Student:
    common_name = None
    name = None
    id = None

    def st(self, name="None", id=0):
        self.name = name
        self.id = id
        print(f"Name {self.name} and Id {self.id} and common_name{self.common_name}")

    def __init__(self, cn=" None "):
        self.common_name=cn

    def get_full_name(self):
        print (self.name, self.common_name)

co = Student("Common name")
co.st(name="Nm1", id=12)
co.get_full_name()
print("------------------")
co2 = Student()
co2.st(name="Nm22", id=14)
co.get_full_name()

common_name, name and id are treated as static variables.

Here

class Student:
    common_name = None
#    name = None
#    id = None

    def st(self, name="None", id=0):
        self.name = name    # 1
        self.id = id # 2
        print(f"Name {self.name} and Id {self.id} and common_name{self.common_name}")

    def __init__(self, cn=" None "):
        self.common_name=cn

    def get_full_name(self):
        print (self.name, self.common_name)

co = Student("Common name")
co.st(name="Nm1", id=12)
co.get_full_name()
print("------------------")
co2 = Student()
co2.st(name="Nm22", id=14)
co.get_full_name()

Even though name and id are getting declared implicitly they are not static variables.
Basically you can keep declaring the variable with self. in class method bodies and keep using them.
But if you declare them explicitly in class body then they are treated as static vars.

>>how to make a python module
The directory needs to have __init__.py, which can be left empty or can have import statements to make it easy

__init__.py
from .Audi import Audi
from .Nissan import Nissan

Audi.py
class Audi:
    def __init__(self):
        print("Exec Audi constructor")

    def print_models(self):
        self.adict = { 'Model1': 'A1', 'Model2': 'A2'}
        print(self.adict)

Nissan.py
class Nissan:
    def __init__(self):
        print("Exec Nissan constructor")

    def print_models(self):
        self.adict = { 'Model1': 'Sentra', 'Model2': 'Rouge'}
        print(self.adict)

All these files should be in a directory called Cars and should be used from outside of the directory like below.


UsingCars.py
from Cars import Nissan
from Cars import Audi

nissan = Nissan()
print(nissan.print_models())

audi = Audi()
print(audi.print_models())


Here, if the __init__.py does not have from .Audi import Audi stateement in it
then in UsingCars.py 

nissan = Nissan() will throw a type error, saying it's not callable.
So, that line should be there. If that line is removed then an explicit call to the constroct should be made
like nissan = Nissan.Nissan() in UsingCars.py


------------------------------------ End --------------------------------------------------
