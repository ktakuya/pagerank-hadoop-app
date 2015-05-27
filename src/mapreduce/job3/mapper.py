#!/usr/bin/env python3

import sys

def main():
    for line in sys.stdin:
        split = line.strip().split('\t')
        print("{0}\t{1}".format(split[1], split[0]))

if __name__ == '__main__':
    main()

