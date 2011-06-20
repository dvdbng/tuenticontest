#!/bin/env python
import sys

# 0 0 0 0
# 1 0 0 0
# 0 1 0 0
# 1 0 1 0
# 0 1 0 1

tests = int(sys.stdin.readline())

for i in range(tests):
    n,t = [int(sys.stdin.readline()) for i in (0,0)]

    light = [str(i) for i in xrange(n) if i<t and (i+t)%2 == 1]
    if len(light) ==0:
        print "All lights are off :("
    else:
        print " ".join(light)


