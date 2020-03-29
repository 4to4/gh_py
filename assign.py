import os
import sys
import argparse


def get_args():
    """Parses input arguments."""
    print(f"Init: Parsing command line arguments.")
    parser = argparse.ArgumentParser(
        description="Program to generate CSV list of pairs of artists appearing together at least 50 times in the "
                    "input file.")
    parser.add_argument(
        '--input_file',
        metavar='FILE',
        default=r'',
        help='Please provide input .csv file.'
    )
    parser.add_argument(
        '--output_file',
        metavar='FILE',
        default=r'',
        help='Please provide output .csv file.',
    )
    # Checking if any of the input arg values are empty.
    empty_args = ','.join(list(k for (k, v) in vars(
        parser.parse_args()).items() if (len(v) == 0)))
    if empty_args:
        print(f"Err : Input args [{empty_args}] are empty. Exiting.")
        sys.exit()

    return vars(parser.parse_args())


def chk_perm_n_get_elig_pairs(input_file, output_file):
    """Call file permission func and create eligible artist dictionary."""

    if not os.access(os.path.dirname(output_file), os.W_OK):
        print(
            f"Err : Destination dir [{os.path.dirname(output_file)}] if not writable. Exiting.")
        sys.exit()
    # Just preliminary check to see if we will be able to create output file in the directory.

    if not os.path.isfile(input_file):
        print(
            f"Err : File [{input_file}] does not exist. Please provide a valid file. Exiting.")
        sys.exit()

    if os.path.getsize(input_file) == 0:  # file is empty
        print(f'Err : Zero bytes input file [{input_file}]. Exiting.')
        sys.exit()

    d_all_artists = {}  # declaring so that I can call .keys() on it
    try:
        with open(input_file, 'r', encoding='utf-8') as f_ro:
            for line_num, line in enumerate(f_ro, start=1):
                # replacing new lines from the artist names
                line = line.replace("\n", '')
                for artist in line.split(','):
                    if artist not in d_all_artists.keys():
                        d_all_artists[artist] = set()
                        d_all_artists[artist].add(line_num)
                    else:
                        d_all_artists[artist].add(line_num)
        print(
            f"Proc: Loaded {[len(d_all_artists.keys())]} artists from input file.")
        return {k: v for (k, v) in d_all_artists.items() if len(d_all_artists[k]) > 49}
    except OSError:
        print(f"Err : {sys.exc_info()[1]}")
        sys.exit()


def get_matching_pairs(d_elig_artists):
    """Collected matching pairs having more than 50 occurrences together."""

    s_matching_pairs = set()  # creating empty set to add to it later
    for key1 in d_elig_artists.keys():
        for key2 in d_elig_artists.keys():
            if key1 != key2:
                if len(d_elig_artists[key1].intersection(d_elig_artists[key2])) > 49:
                    s_matching_pairs.add(f"{','.join(sorted([key1, key2]))}\n")
    print(f"Proc: Collected {[len(s_matching_pairs)]} matching pairs.")
    return s_matching_pairs


def write_matching_pairs(output_file, s_matching_pairs):
    """Write sorted pairs to the output file."""
    try:
        with open(output_file, 'w', encoding='utf-8') as f_rw:
            for line in s_matching_pairs:
                f_rw.write(line)
    except OSError:
        print(f"Err : {sys.exc_info()[1]}")
        sys.exit()

    print(
        f"Proc: Wrote {[len(s_matching_pairs)]} matching pairs to {[output_file]} file.")
    print(f"Info: Exiting.")


# main
def main():
    d_ip_vals = get_args()
    d_elig_artists = chk_perm_n_get_elig_pairs(
        d_ip_vals['input_file'], d_ip_vals['output_file'])

    if not d_elig_artists:
        print("No artist is appearing on more than 49 lines. Exiting")
        sys.exit()

    s_matching_pairs = get_matching_pairs(d_elig_artists)
    if not s_matching_pairs:
        print("Zero artist pairs found appearing together for more than 49 times. Exiting")
        sys.exit()

    write_matching_pairs(d_ip_vals['output_file'], s_matching_pairs)


# main
if __name__ == "__main__":
    main()
