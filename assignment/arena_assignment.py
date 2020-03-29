import os
import sys
import argparse

# Get command line arguments
def get_args():
    parser = argparse.ArgumentParser(
        description="Program to generate CSV list of pair of artists appearing together at least 50 times in the input file.")
    parser.add_argument(
        '--input_file',
        metavar='FILE',
        default=r'D:/dev/arena_assignment/Artist_lists_small_big.csv',
        help='Please provide a valid .csv file.'
    )
    parser.add_argument(
        '--output_file',
        metavar='FILE',
        default=r'D:/dev/arena_assignment/outfile.csv',
        help='Please .csv file path to write the output.',
    )

    print(f"Init: Parsed command line arugments.")
    return vars(parser.parse_args())


# Validate files and create file handles
def get_fhs(input_file, output_file):
    try:
        if (os.path.isfile(input_file) == False):
            print(
                f"Err : File [{input_file}] does not exist. Please provide a valid file. Exiting.")
            exit()

        if(os.path.getsize(input_file) == 0):
            print(
                f"Err : File [{input_file}] is zero bytes. Please provide a valid file. Exiting.")
            exit()
    except (OSError):
        print(f"Err : {sys.exc_info()[0]}")
        exit()

    f_ro = open(input_file, 'r', encoding='utf-8')

    try:
        f_rw = open(output_file, 'w', encoding='utf-8')
    except (OSError):
        print(f"Err : {sys.exc_info()[1]}")
        exit()

    print(f"Init: Validated ip/op files & created file handles.")
    return (f_ro, f_rw)


# Make main artists dict
def get_main_artist_dict(f_ro):
    line_num = 1        # line numbers from the file
    d_all_artists = {}  # all artists dictionary

    for line in f_ro:
        # replacing new lines from the artist names
        line = line.replace("\n", '')
        for artist in line.split(','):
            if not artist in d_all_artists.keys():
                d_all_artists[artist] = set()
                d_all_artists[artist].add(line_num)
            else:
                d_all_artists[artist].add(line_num)
        line_num += 1
    print(f"Info: Loaded input_file data.")
    return d_all_artists


# Create a dict for artists appearing on more than 50 lines
def make_50plus_artist_dict(d_all_artists):
    d_elig_artists = {}
    for k in d_all_artists.keys():
        if len(d_all_artists[k]) < 50:
            continue
        else:
            d_elig_artists[k] = d_all_artists[k]
    print(f"Info: Created eligible data set of artists.")
    return d_elig_artists


# Collected matching pairs having more than 50 occurrances together
def get_matching_pairs(d_elig_artists):
    s_matching_pairs = set()
    for key1 in d_elig_artists.keys():
        for key2 in d_elig_artists.keys():
            if key1 == key2:
                continue
            if len(d_elig_artists[key1].intersection(d_elig_artists[key2])) >= 50:
                s_matching_pairs.add(f"{key1},{key2}\n")
    print(f"Info: Collected matching pairs.")
    return s_matching_pairs

# Writing the pairs to the output file
def write_matching_pairs(f_rw, s_matching_pairs):
    for pair in s_matching_pairs:
        f_rw.write(pair)
    print(f"Info: Wrote matching pairs to output file.")
    print(f"Info: Exiting.")


# main
def main():
    d_ip_vals = get_args()
    (f_ro, f_rw) = get_fhs(d_ip_vals['input_file'], d_ip_vals['output_file'])

    d_all_artists = {}    # all artists name to line_numbers dictionary
    d_elig_artists = {}   # all artists appearing on more than 50 different lines
    s_matching_pairs = set()  # artist pairs appearing together for 50 or more times

    d_all_artists = get_main_artist_dict(f_ro)
    d_elig_artists = make_50plus_artist_dict(d_all_artists)
    s_matching_pairs = get_matching_pairs(d_elig_artists)
    write_matching_pairs(f_rw, s_matching_pairs)


#### main ####
if __name__ == "__main__":
    main()

