# Typical python function
import sys
import traceback

def func1(i, j, k="XX"):
    print(f"1: {i} \n2: {j}")
    print(f"Opt arg {k}") if (k) else ()

func1("arg1", "arg2")

# Python supports named parameters, so that ordering should not matter e.g.
func1(i="yo", j="mana") # One must know the names of the input parameters of the function for that
func1(j="yo", i="mana", k="FF") # One must know the names of the input parameters of the function for that
func1(j="mama", i="yo")

#optional arguments are supported with default value already specified
#They will be used / printed only if they are specified like K



# *args holds argument but as a list e.g.
def all_args(i, *args):
    print(f"first arg {i}")
    print(f"All args {args}")

all_args(1, 3434, 3466 )
# here the first argument is printed separately and second separately
# to avoid this, catch all these args with **kwargs which will turn these args into dictionary

def all_kwargs(i, **kwargs):
    print(f"first arg {i}")
    print(kwargs)

all_kwargs("Yo_name", desc="DEDEDE", fb="Feedback", other="OTHER")
#notice that first arg is positional where as rest of them are captured as dictionary

# Yield

def yfunc():
    for i in range(10):
        print(f" -> {i}")
        yield i
    return

def ycall():
    for i in yfunc():
        print(i)

ycall()

# one of the function a producer and other is comsumer. producer is has keywork yield in it
# consumer calls producer. Producer keeps the image on hold until the next one is called.

# Here Yield stores the process image, in registers and stack when the yield is called
# and loads it back when called the next time.

# The idea is to process only one data set at a time from the calling function, This saves memory and time


#lamda functions
# regular function looks like:

def reg_func(i):
    print("Yo man", i + i)

#calling it
reg_func(9)

# lamnda function
twice = lambda i: i+i

print(twice(4))







