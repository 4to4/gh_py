import json

js = '''
{
    "people": [
        {
            "first-name": "Jane", 
            "last-name": "Roe", 
            "email2": "jane.roe@example.com"
        }, 
        {
            "first-name": "John", 
            "email2": "john.doe@example.com",
            "last-name": null
        }
    ]
}'''


# json.loads function
data = json.loads(js) # 1. To load the files
#2. lists get converted to arrays, null to None, Str - string, whole thing to dict.
print(data)

# iterating through
for p in data['people']:
    print(f"P -> {p}")

# dump() is used to write to a file
# dumps() is used to write to a string and use it later.

#dumping json
for p in data['people']:
    del p['first-name']

# json.dumps function - s string 
jstr = json.dumps(data, indent=2) # here 2 is number of indention - make it easy to read
print(jstr)

# dumping with sorted keys
jstr = json.dumps(data, indent=2, sort_keys=True)
print(jstr)

# load json as file object

with open(r'D:\dev\large_dataset\rows.json', encoding='utf-8') as f:
    data = json.load(f)

# print(data)
# similarly the dump function 

with open('output_file', 'w', encoding='utf-8') as f:
    json.dump(data,f)

print('dumped')

