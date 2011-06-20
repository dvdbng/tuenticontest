#!/bin/env python

import sys

for line in sys.stdin:
    a,b = line.split()
    matrix = [
        [0 for j in xrange(len(b)+1)] for i in xrange(len(a)+1)
    ]
    longest = 0
    pos = 0
    for x in xrange(1,len(a)+1):
        for y in xrange(1,len(b)+1):
            if a[x-1] == b[y-1]:
                matrix[x][y] = matrix[x-1][y-1] + 1
                if matrix[x][y]>longest:
                    longest = matrix[x][y]
                    pos = x-longest
            else:
                matrix[x][y] = 0
    print a[pos:pos+longest]
