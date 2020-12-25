import sys


def f():
    str = "Yo_mama"
    # print("This string is {} {}".format(str,'1'))
    # print("xyz {2} {1} {0}".format(1, 2, 3))
    # print(f"This string has {str} values in it")

    # print("Dictionaries are perl hashes")
    # print("Tuples are const arrays")
    # print("Arrays are list")
    # print("Sets unordered lists with unique elements, heterogenous")

    d = {"a": 1, "b": 3}
    print(d)
    print(
        dict(
            enumerate("Where is this string".split(), start=1)
        )
    )

    for k, v in enumerate(d):
        print(f"K{k} V{v}")

    s1 = {1, 2, 2, 3, 3, 3, 3, 3, 35, 5, 5, 5, "A"}
    print(s1)

    print(1 in s1)

    print('Y') if (1 in s1) else "N"

    l = list([1, 2, 2, 3, 3, 3])
    print(l[4])

    dict2 = {4: 34, 12: 34, 5: 23434, 1: 65765, 654645: 1}
    for i in sorted(dict2.keys(), key=int):  # this will sort the list numerically
        print(f"K:{i}  V:{dict2[i]}")

    # list comprehension
    words = "Where is my mba I do not see it yet"
    len_lst = [len(word) for word in words.split() if word != "is"]
    print(len_lst)

    # dictionary comprehension
    words = "this is dict comprehension"
    d_c = {word: len(word) for word in words.split() if len(word) > 2}
    print(d_c)

    # set comprehension
    words = "this is set comprehension"
    s_c = set(
        len(word) for word in words.split() if len(word) > 2
    )
    print(s_c)

    # generator comprehension
    words = "This is generator comprehension"
    g_c = (len(word) for word in words.split() if len(word) > 2)

    for i in g_c:
        print(f"Gen {i}")

    # gen = (len(word) for word in words)
    # print("Generator comprehension", type(gen), gen)
    # for i in gen:
    #     print(f"Gen comprehension Elements {i}")
    # print("-------------------------------------")


if (__name__ == '__main__'):
    f()
else:
    print("No main")



#bytes in python
b1 = b'data'
print(b1)



#-------------------------- load json

import json

with open(r'D:\dev\large_dataset\rows.json', encoding='utf-8') as f:
    data = json.load(f)

print(json.dumps(data, indent=2, sort_keys=True))