#!/usr/bin/env python
# coding: utf-8

import sys

DAMPING = 0.85

def pagerank(title, links_list):
    is_exist = False
    links = ""
    sum_ranks = 0.0
    for page in links_list:
        if page[0] == "!":
            is_exist = True
            continue
        if page[0].startswith("|"):
            page[0] = page[0][1:]
            links = "\t" + "\t".join(page)
            continue
        rank = float(page[1])
        count_outlinks = int(page[2])
        if count_outlinks != 0:
            sum_ranks += (rank / count_outlinks)

    if not is_exist:
        return
    new_rank = DAMPING * sum_ranks + (1.0 - DAMPING)
    print("{0}\t{1}{2}".format(title, new_rank, links))

def main():
    links = []
    now = ""
    while True:
        try:
            line = sys.stdin.readline()
            if not line:
                break
            splited = line.strip().split('\t')
            if splited[0] != now:
                if now != "":
                    pagerank(now, links)
                now = splited[0]
                del links
                links = []
            links.append(splited[1:])
        except Exception as e:
            sys.stderr.write(str(e))
            continue
 
if __name__ == '__main__':
    main()

