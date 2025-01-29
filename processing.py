#!/usr/bin/env python3

file = open('offers_urls.txt', 'r')

for line in file:
    line = line.strip()[28:]
    print(line)