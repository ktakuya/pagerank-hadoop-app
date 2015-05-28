#!/usr/bin/env python
# coding: utf-8

import sys

def main():
    while True:
        try:
            line = sys.stdin.readline()
            if not line:
                break
            split = line.strip().split('\t')
            print("{0}\t{1}".format(split[1], split[0]))
        except Exception:
            continue

if __name__ == '__main__':
    main()

