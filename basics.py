print ("\n\n***** This program will cover all the Python Programming language basics!! ******\n\n")

print("\t Handling strings. Python has single line string which can use single \' or double quote \". There is no difference in them.")
print("\t A multi line strings is printed using triple quotes, single of double does not matter. e.g. \"\"\" or \'\'\'")
print("\t Example of multi line string:")

print("""Here
is
another
string""")

print("\tString are also arrays in Python")
string = 'YoYo Man'
print("Full string is " + string + "\n")
print("First 5 elements of the string " + string[0:4])

# print("out of range arrays" + string[122]) This fails.

str = "Yo_mama"

print(str.count)

print("DD", str[5])

print (str.replace('o', 'T'))

print(str.rfind('a'))
print(str.rindex('m'))

str = '{}, {} This is string'.format(str, '1')
print(str)

str = f'{str.upper()} This is outter string now. {"and this is innder".upper()}'
print(str)

print(dir(int))
print(help(int.real))


#####################################################################################################################################################################

print("Dictionaries:.... are Hashes in Perl.....")
student = {'name': 'A', 'age': '23', 'cor': ['A', 'B']}

print(student['name'])
print(student['cor'][1]) # looks like two dimensional array but it's not. It's how to access the list in dictionary

print(student.get('XXX')) # if accessed a key via get method that does not exist then get method returns Node
print(student.get('XXX', 'NOT FOUND')) # if accessed a key via get method that does not exists but want to display custom message then use get method with second argument as custom argument and that will be displayed

print(student)

# to update multiple values in one shot use update method
student.update({'name': 'XXXX'})
print(student)

#delete a key from dict
del student['age']
print(student)

#print number of keys in a dictionary
print(len(student))

for key, value in student.items():
    print ('\tKey => [{}]. Value => [{}]'.format(key, value))

################################################### Lists, Sets and Tuples #############################

# > list = array
listis = [ 'a', 'b', 'c', 'd', 'e']
print(len(listis))
print(listis[2])

#print(listis[5]) # this is error
print(listis[1:2]) # second index is not included

print(listis[1:])
print(listis[:3])

print(listis[-1])

#add an items to a list
listis.append('ART')
print(">", listis)

#insert a value at a specific index
listis.insert(2, 'NoArt')
print(">>", listis)

#adding a list to a list
listis2 = ['X', 'Y']
listis.insert(2, listis2)
print ('>>>>>', listis)
print("...:", listis[2][1]) # printing list element inside a list

# extending a list, meaning adding elements of a list at end of another list
listis.extend(listis2)
print("Extended list is", listis)

# removing a value from list using a value
listis.remove('X')
print(listis)

# using pop
print(listis.pop()) #pop returns what's removed that is the last in element
print(listis)

#remove element by index using pop
print(listis.pop(2))

l1 = [ 'H', 'M', 'P', 'C']
print ( l1 )

print ('H' in l1)

for index, item in enumerate(l1, start=1):  #this function will return value and index
    print(index, item)

# join and split
print('-'.join(l1)) # joined string by delim
print('a-a-b-s-d-r-d'.split('-')) # this is returning array (list)

# > tuples are const arrays
print("\n\n\nNow learning const arrays which is Tuples. Uses paranthesis instead of square brackets\n\n\n")
t1 = ('A', 'B', 'C', 'D', 'E', 'F')
print( t1 )

for i, v in enumerate(t1):
    print(i, v)

# > sets are unordered const arrays uses curly braces . sets are hashes, removes dupes and optimized for access
print("\n\n\nNow learning const arrays which are unordered. Uses curly braces\n")
set1 = { 'a', 'b', 'c', 'd', 'e', 'f'}
print ( 'a' in set1 )
print(set1.union({'1', '2'}))

