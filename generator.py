import itertools
def gen123():
    yield 1
    yield 2
    return

g = gen123()
print(next(g))
print(next(g))


# refer https://stackoverflow.com/questions/1756096/understanding-generators-in-python

# febonacci series
def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

ip_list = ', '.join((str(x) for x in list(itertools.islice(fib(),10))))
print(ip_list)