import requests
import sys

"Download and write files."

# download and write a file
resp = requests.get(r'https://www.w3.org/TR/PNG/iso_8859-1.txt')
assert (resp.ok),  "Could not download!" # using perl's "or die "die msg". Operational only if optimization not turned on."

# resp.iter_content - gives a generator to iterate through the file contents
for line in (resp.iter_content()): # stores in binary
    pass
    # print(line)

# whole file can be downloaded with resp
resp = requests.get(r'https://www.w3.org/TR/PNG/iso_8859-1.txt')
assert (resp.ok), "Failed download!"
data = resp.text # stores all of it in binary
for line in data:
    pass
    # print(line)

# whole file can be downloaded with resp
resp = requests.get(r'https://www.w3.org/TR/PNG/iso_8859-1.txt')
assert (resp.ok), "Failed download!"
with open(r'local_file.txt', 'wb', buffering=10) as w:
    w.write(resp.content)


