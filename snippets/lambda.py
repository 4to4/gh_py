d = dict(
            enumerate
            (
                    "Where 1 is 3 the 4 perfect 34 tutorial 3434 for 3434 3 this".split(), start=1
            )
        )

# lambda format: lambda <argument>: <function_body>, <list>
filter_obj = list(filter(lambda x: x.isalpha(), d.values()))


# filter is like perl map function with a context
# filter returns object of filter class which has to be type casted into list / dict etc.
print(list(filter_obj))
print(set(filter_obj))
print(tuple(filter_obj))


