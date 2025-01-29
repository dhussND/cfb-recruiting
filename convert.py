#!/usr/bin/env python3

file = open('player-offerlist-url.txt', 'r')
line = file.readline()
eval(line)
print(line)