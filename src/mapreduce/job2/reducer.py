#!/usr/bin/env python3

import sys

DAMPING = 0.85

pages_dict = {}

for line in sys.stdin:
    splited = line.strip().split('\t')
    if not splited[0] in pages_dict:
        pages_dict[splited[0]] = []
    pages_dict[splited[0]].append(splited[1:])

for key, values in pages_dict.items():
    is_exist = False
    links = ""
    sum_ranks = 0.0

    for page in values:
        if page[0] == "!":
            is_exist = True
            continue
        if page[0].startswith("|"):
            page[0] = page[0][1:]
            links = "\t" + "\t".join(page)
            continue
        rank = float(page[1])
        count_outlinks = int(page[2])
        sum_ranks += (rank / count_outlinks)

    if not is_exist:
        continue
    new_rank = DAMPING * sum_ranks + (1.0 - DAMPING)
    print("{0}\t{1}{2}".format(key, new_rank, links))
