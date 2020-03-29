import pandas as pd
import sys
import os

# make main artists dict #
def get_main_artist_dict(ip_filename): 

    if (os.path.isfile(ip_filename) == False):
        print(f"File [{ip_filename}] does not exist. Please provide a valid file. Exiting.")
        exit()

    if(os.path.getsize(ip_filename) == 0 ):
        print(f"File [{ip_filename}] is zero bytes. Please provide a valid file. Exiting.")
        exit()

    try:
        main_df = pd.read_csv(ip_filename, skip_blank_lines=True)
        rows = main_df.axes[0]
        columns = main_df.axes[1]
    except (OSError):
        print("An I/O error has occured. Try again")
        exit()
    return main_df
        

def main():
    input_file = r'D:/dev/arena_assignment/Artist_lists_smal_big.csv'
    output_file = r'D:/dev/arena_assignment/outfile.csv'
    main_df = get_main_artist_dict(input_file)
    # print(main_df)

main()

"""
#with open(r'D:/dev/arena_assignment/artist.csv', encoding='utf-8') as f:
input_file = r'D:/dev/arena_assignment/Artist_lists_small_big.csv'
output_file = r'D:/dev/arena_assignment/outfile.csv'

with open(input_file, encoding='utf-8') as f:
    for line in f:
        line.replace("\n", "")
        for artist in line.split(','):
            if not artist in dict_main.keys():
                dict_main[artist] = set()
                dict_main[artist].add(line_num)
            else:
                dict_main[artist].add(line_num)
        line_num += 1


#pick only the artists who are appearing more than 50 times
fifty_plus_artists = {}

for k in dict_main.keys():
    if len(dict_main[k]) < 50:
        continue
    else:
        fifty_plus_artists[k] = dict_main[k]


w = open(output_file, 'w', encoding='utf-8')
pairs_to_write = set()
for key1 in fifty_plus_artists.keys():
    for key2 in fifty_plus_artists.keys():
        if key1 == key2:
            continue
        if len(fifty_plus_artists[key1].intersection(fifty_plus_artists[key2])) >= 50:
            pairs_to_write.add(f"{key1},{key2}")
            w.write(f"{key1},{key2}\n")
            

print(pairs_to_write)

# with open(output_file, 'w', encoding='utf8') as f:
#     f.write(text)
"""