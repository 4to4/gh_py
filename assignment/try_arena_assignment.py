import os
import csv
import sys

artist_set = set()
with open('D:/dev/arena_assignment/artist.csv', encoding='utf-8') as f:
  for line in f:
    s1 = list(line.replace("\n", "").split(','))
    print(s1)

artist_set.update(s1)
# sys.stdin.read(1)
print(len(artist_set))
print(artist_set)


#file_handle = open("D:/dev/arena_assignment/Artist_lists_small.csv", "r")



# if os.path.exists(file_name):
#     with open(file_name, 'r') as file_handle:
#         reader = csv.reader(file_handle)
#         for row in reader:
#             print(f"ROW -> {row}")
#             sys.stdin.read(1)


