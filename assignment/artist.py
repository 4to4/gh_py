import pandas as pd
import numpy as np
import sys


input_file = "D:/dev/arena_assignment/artist.csv"
artist = pd.read_csv("D:/dev/arena_assignment/artist.csv")
print(f"Input file {input_file} loaded.")
print("Shape: ", artist.shape)
print("Data frame info", artist.info())
artist.info(memory_usage='deep')

print(artist.head())

# for i in artist.iterrows():    print(i)


# df = pd.DataFrame()
# print(artist.aggregate)
# print(artist.columns) No headers needed
# print(artist.Series)




#artist.Series()


# for i in artist:
#     print(i)
#     sys.stdin.read(1)

# print(artist.head())
# pd.Series.str.count()


