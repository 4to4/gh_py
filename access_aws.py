import json
import boto3

s3 = boto3.resource('s3')

def lambda_handler(event, context):
    bucket_list = []
    print(s3)


#-----------------------

# generator comprehension
for i in ( x for x in ("this is text".split()) if len(x) > 2):
    print(i)

# dictionary comprehension
print( type({ x:y for x,y in (enumerate(list("xyz"),start=1)) if x > 1}) )

for k,v in ({ x:y for x,y in (enumerate(list("xyz"),start=1)) if x > 1}.items()):
    print(k)


# print(sorted(dict(a=1, b=2, c=2),key=lambda x: x[0]))
# print(sorted(dict(a=1, b=2, c=2),key=lambda x: x[1]))
print("ffffffff")
st = dict(enumerate("this is test".split(), start=1))

print( sorted(st.items(), key = lambda x: x[0]) )
print( sorted(st.items(), key = lambda x: x[1]) )
print("ffffffff")
# d = dict()
# print(sorted(d.items(), key = lambda x: x[0])) # sort by key
# print(sorted(d.items(), key = lambda x: x[1])) # sort by values


st = " this is test "
d = dict(
        enumerate(
                    st.split(), start=1
                )
        )

for k,v in sorted(d.items(), key=lambda item: item[1]):
    print("%s: %s" % (k, v) )