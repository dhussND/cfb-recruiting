#!/usr/bin/env python3

import collections

file = open('filenames.txt', 'r')
offer_count_by_school = collections.defaultdict()


for line in file:
    line = line.strip()
    string = f"./offers/{line}"
    f = open(string, 'r')
    for offer in f:
        offer = offer.strip()
        offer_count_by_school[offer] = offer_count_by_school.get(offer, 0) + 1
    f.close()

# for school, count in offer_count_by_school.items():
#     print(f"{school}: {count}")

for school, count in dict(sorted(offer_count_by_school.items(), key=lambda item: -item[1])).items():
    print(f"{school}: {count}")    
