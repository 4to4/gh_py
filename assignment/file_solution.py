import os
import csv
import sys

artist_set = set()
with open('D:/dev/arena_assignment/artist.csv', encoding='utf-8') as f:
  for line in f:
      line = line.strip()
      line = line.lower()
      s1 = line.split(',')
      for a in s1:
          print(f"A -> {a}")


# artist_set.update(s1)
# sys.stdin.read(1)
print(len(artist_set))
print(artist_set)

