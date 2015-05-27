#!/usr/bin/env python3

import sys

def main():
    id_to_title = {}
    links_dict = {}
    # Input
    for line in sys.stdin:
        try:
            page_id, which, title = line.strip().split('\t')
            if which == 'p':
                id_to_title[page_id] = title
            elif which == 'l':
                if not page_id in links_dict:
                    links_dict[page_id] = []
                links_dict[page_id].append(title)
        except Exception:
            continue

    # Output
    for page_id, title in id_to_title.items():
        try:
            if not page_id in links_dict:
                print("{0}\t1.0".format(title))
                continue
            print("{0}\t1.0\t{1}".format(title, "\t".join(links_dict[page_id])))
        except Exception:
            continue

if __name__ == '__main__':
    main()

