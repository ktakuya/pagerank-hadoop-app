#!/usr/bin/env python
# coding: utf-8

import sys
import doctest

def page_split(row):
    """ Split string and return page_id and page_title
    >>> page_split("1,4,'アップロードログ_2004年4月','sysop',498,0,0,0.00326005555992951,'20150420034300',NULL,2168855,106607,NULL")
    ('1', 'アップロードログ_2004年4月')
    """
    c1 = row.find(',')
    c2 = row[c1+1:].find(',') + c1 + 1
    c3 = row[c2+1:].find("','") + c2 + 2

    page_id = row[:c1]
    page_title = row[c2+1:c3]
    return page_id, page_title[1:-1]

def pagelinks_split(row):
    """ Split string and return pl_from and pl_title
    >>> pagelinks_split("7688,0,'2&4モータリング社',0")
    ('7688', '2&4モータリング社')
    """
    c1 = row.find(',')
    c2 = row[c1+1:].find(',') + c1 + 1
    c3 = row.rfind(',')

    pl_from = row[:c1]
    pl_title = row[c2+1:c3]
    return pl_from, pl_title[1:-1]

def main():
    for line in sys.stdin:
        line = line.strip()
        if line.startswith('p'):
            page_id, page_title = page_split(line[1:])
            print("{0}\tp\t{1}".format(page_id, page_title))
        elif line.startswith('l'):
            pl_from, pl_title = pagelinks_split(line[1:])
            print("{0}\tl\t{1}".format(pl_from, pl_title))

if __name__ == '__main__':
    # doctest.testmod()
    main()

