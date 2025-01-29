#!/usr/bin/env python3

import os
import json
import re

file = open('../names.txt', 'r')

# List of URLs to process
players = []

for line in file:
    line = line.strip()[3:] + " }"
    line = json.loads(line)
    processed_name = re.sub(r'[^a-zA-Z]', '', line["name"]).lower()
    players.append(processed_name)


i = 0
file = open('../offers_urls.txt', 'r')
for line in file:
    line = line.strip()
    string = f"curl -s {line} | grep -oP '(?<=2025-Football/Commits/\">).+?(?= </a>)' > {players[i]}_offers.txt"
    os.system(string)
    i += 1
