#!/bin/env python
import sys


num = int(sys.stdin.readline())
for i in xrange(num):
    tank,distance,stations = [int(sys.stdin.readline()) for i in range(3)]
    stations = map(int,sys.stdin.readline().split())
    last_fueled = 0
    fueled = []
    for i in range(len(stations)+1):
        if (stations[i] if i<len(stations) else distance)-last_fueled > tank:
            fueled.append(stations[i-1])
            last_fueled = stations[i-1]

    if len(fueled) == 0:
        print "No stops"
    else:
        print " ".join(map(str,fueled))

