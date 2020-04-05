import os
import sys

# 1. lst.append("X" - appends to the list
# Adds an element at the end of the list
# append function adds to a list
lst = list("This is a list".split())
print(lst)
lst.append("NewElement")
print(lst)
##########################################

# 2. lst.remove() - returns None
# Empty a list - lst.remove()
# Removes all the elements from the list
print(lst.clear())
lst = list("This is a list again".split())
print(lst)
##########################################

# 3.shallow copy of a list
# shallow copy means a new copy of the list is made but the elements in the list are
# pointing to the old list elements. Two ways to make shallow copy

# a.
new_lst = lst.copy()
print(id(new_lst[1]))
print(id(lst[1]))
print(new_lst[1] is lst[1])

# b. This only copies the reference of the variable and create new reference variable
new_lst2 = lst
print(new_lst2 is lst)
# Notice element[0] is pointing to the same element

# 4. Deep copy - makes a full copy of the array, with every element
# but deep copy is useful only for nested mutable objects, like list of lists
# deep copy needs to import module called copy

import copy

a = list("qwerty is just a string".split())
b = list("This list is x")
d = (a, b)
e = copy.deepcopy(d)
print(id(d[0]) == id(e[0]))
print("Are the elements identical", d[0] is e[0])
# Deep copy will not make effect if this runs on simple lists and not list of lists
# i.e. nested lists
##########################################

# 5. - returns the number of elements with specified value
# Returns the number of elements with the specified value
lst = list("This is a mask".split())
print(len(lst))
##########################################

# 6. Add elemts of a list to end of current list
lst = list("This is the mask".split())
print(lst.extend("A B C".split()))

# if you use append then the whole list will become the last element of the original list
lst.append(list("Not the mask".split()))
print(lst)
##########################################


# Returns the index of the first element with the specified value
print(lst.index("the"))
##########################################

# Adds an element at the specified position
print(lst.insert(1, "X"))
print(lst)
##########################################

# Removes the element at the specified position, returns the removed element
print(lst.pop(1))
print(lst)
##########################################

# Removes the first item with the specified value
lst.remove("the")
print(lst)
##########################################

# Reverses the order of the list - reverses the order in place
rlst = list("ABC")
rlst.reverse()
print(rlst)
##########################################


# sort - inplace permanently sorted
# sorted - temporarily sorted and returns the sorted instance
lst = list("You shall not pass.".split())
lst.sort()
print(lst)

lst = list("BCA")
print(sorted(lst))
print(lst)
###########################################

# sort reserver true
print("##############################")
lst = list("ABC123")
print("Reverse True")
lst.sort(reverse=True)
print(lst)

# sort reserver false
lst = list("ABC123")
print("Reverse False")
lst.sort(reverse=False)
print(lst)

print("##############################")
# sorted with key argument
lst = list("You shall not pass".split())
print(sorted(lst, key=len, reverse=True))
print(sorted(lst, key=len, reverse=False))

# lst = list("ZAS FDASFDY 13434 2123243".split())
# print(sorted(lst, key=lambda x: reversed(x), reverse=True))


lst = [('candy', '30', '100'), ('apple', '10', '200'), ('baby', '20', '300')]
lst = list("123 234 456".split())  ### - ???????


def lf(x):
    print(x[2])
    return x[2]


lst.sort(key=lf)
print(lst)

# "ABC123".split().sort(reverse=False)
# print("Reverse True", lst)

# print(lst)
