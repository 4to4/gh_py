import math

x = 1000
x = 2
print(x)

print(id(x))
print((x is x))

k = [9,9,7,0]

def modify(k):
    k.append(435)
    print(k)

modify(k)

def banner2(msg, banner='-'):
    print("msg is {msg} and banner is {banner}\n")
banner2("TTITI", 343443)


def banner(msg="Default msg", border_char='-'):
    line = border_char * len(msg)
    print(line)
    print(msg)
    print(line)

banner()
banner(msg='New msg', border_char='*')
banner(msg='Brand New msg', border_char='^')


print(type(math))
print(dir(math))

print(math.sin.__doc__)