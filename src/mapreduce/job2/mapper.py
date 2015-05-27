#!/usr/bin/env python3

import sys

PAGE_INDEX = 0
RANK_INDEX = 1
LINKS_INDEX = 2

def main():
    while True:
        try:
            line = sys.stdin.readline()
            if not line:
                break
            row = line.strip().split('\t')
            page, rank = row[PAGE_INDEX], row[RANK_INDEX]
            print("{0}\t!".format(page))
            if len(row) == 2:
                continue
            links = row[LINKS_INDEX:]
            total_links = len(links)
            for other in links:
                print("{0}\t{1}\t{2}\t{3}".format(other, page, rank, total_links))
            print("{0}\t|{1}".format(page, "\t".join(links)))

        except Exception:
            continue

if __name__ == '__main__':
    main()

