#!/usr/bin/env python
"""
The attached utf-8 encoded text file contains the favorite musical artists of 1000 users from LastFM. Each line is a list of up to 50 artists, formatted as follows:
     
    Radiohead,Pulp,Morrissey,Delays,Stereophonics,Blur,Suede,Sleeper,The La's,Super Furry Animals\n Band of Horses,Iggy Pop,The Velvet Underground,Radiohead,The Decemberists,Morrissey,Television\n
etc.
Write a program that, using this file as input, produces a list of pairs of artists which appear TOGETHER in at least fifty different lists. For example, in the above sample, Radiohead and Morrissey appear together twice, but every other pair appears only once. Your program should output the pair list to stdout in the same form as the input (eg Artist Name 1, Artist Name 2\n).
You MAY return an approximate solution, i.e. lists which appear at least 50 times with high probability, as long as you explain why this tradeoff improves the performance of the algorithm.
"""

import os
import sys

fh = open(r'd:/dev/arena_assignment/Artist_lists_small.txt', 'rb')

pair_counts = {}
pair_lines = {}

lines = []

def pair_up(artists):
    pairs = []

    for idx, first in enumerate(artists):
        # the last element is already paired up, so quit
        if idx == len(artists)-1:
            break

        for second in artists[idx+1:]:
            pairs.append(tuple(sorted([first, second])))

    return pairs

line_number = 0
while True:
    line = fh.readline()

    if line == '':
        break

    line_number += 1

    if line.strip() == '':
        continue

    sys.stderr.write('\r' + str(line_number))
    sys.stderr.flush()

    for pair in pair_up(line.strip().split(',')):
        if pair not in pair_counts:
            pair_counts[pair] = 1
            pair_lines[pair] = []
        else:
            pair_counts[pair] += 1
            pair_lines[pair].append(line_number)

favorite_pairs = set()
pair_lines_union = None
for pair, count in pair_counts.items():
    if count >= 50:
        favorite_pairs.add(pair)
        lines_set = set(pair_lines[pair])

        if pair_lines_union is None:
            pair_lines_union = lines_set
        else:
            pair_lines_union.update(lines_set)

sys.stderr.write('\r')
print >> sys.stderr, 'favorite pairs:', sorted(favorite_pairs)

favorite_artists = set()
for item in favorite_pairs:
    favorite_artists.update(set(item))
print >> sys.stderr, 'favorite artists:', sorted(favorite_artists)

lines_to_print = sorted(list(pair_lines_union))

fh.seek(0, 0)

line_number = 0
while True:
    line = fh.readline()

    if line == '':
        break

    line_number += 1
    if line_number == lines_to_print[0]:
        sys.stdout.write(line)
        sys.stdout.flush()

        lines_to_print.pop(0)

    if not lines_to_print:
        break

fh.close()

"""
import pandas as pd

## added and extra Jones into row 1 for 'Jan' column
sales = [{'account': 'Jones LLC', 'Jan': 'Jones', 'Feb': '200', 'Mar': '140'},
         {'account': 'Alpha Co',  'Jan': 'Jones', 'Feb': '210', 'Mar': '215'},
         {'account': 'Blue Inc',  'Jan': '50',  'Feb': '90',  'Mar': '95' }]

df = pd.DataFrame(sales)

df_list = []

for search_string in ['Jones', 'Co', 'Alpha']:
    #use above method but rename the series instead of setting to
    # a columns. The append to a list.
    df_list.append(df.apply(lambda x: x.str.contains(search_string))
                     .sum(axis=1) ## HERE IS SUM in place of any
                     .astype(int)
                     .rename(search_string))

#concatenate the list of series into a DataFrame with the original df
df = pd.concat([df] + df_list, axis=1)
print(df)


import pandas as pd

sales = [{'account': 'Jones LLC jones', 'Jan': '150', 'Feb': '200', 'Mar': '140 jones jones'},
         {'account': 'Alpha Co',  'Jan': 'Jones', 'Feb': '210', 'Mar': '215'},
         {'account': 'Blue Inc',  'Jan': '50',  'Feb': '90',  'Mar': '95' }]
df = pd.DataFrame(sales)
df

search_string = 'Jones'

(df.apply(lambda x: x.str.contains(search_string)).sum(axis=1).astype(int))
"""




"""
str1 = '19yrs of experience in managing, leading, building, apps, services, teams in finance infrastructure for broker dealer services, tri-party repo, hedge funds and deployment etc. •	Strong management, prioritization, planning, architectural skills in the field of product management, product development, relationship mgmt., team mgmt. etc. •	Built, enhanced and managed many critical milestone financial and infrastructure services e.g. credit monitoring, market/security reference data, trade mgmt., global deployment •	Specialized in modernization/consolidation, technology mgmt., outsourcing and cost savings for medium/large critical applications on various platforms. •	Thorough at managing resources, risk, delivery, cost and product management. in modern. •	Exceptional blend of hard and soft skills ranging from process methodology to risk mgmt., learning agility team building and interpersonal effectiveness. •	Managed and mentored teams, acquired hands on leadership and management skills and grown into an adept, goal oriented management professional in last 12 years. •	Self-taught tri-party repo, prime brokerage, hedge funds, merchant services, software deployment businesses and acquired in depth business and technical knowledge.'.split()

print(type(str1))

for s in str1:
    print(f"{s} => {str1.count(s)}")
"""