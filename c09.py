#!/bin/env python
import sys

actions = {}

def readkey():
    key = sys.stdin.readline().split()
    key.sort()
    return " ".join(key)

num = int(sys.stdin.readline())
for i in xrange(num):
    key = readkey()
    actions[key] = sys.stdin.readline().strip()

tests = int(sys.stdin.readline())
for i in xrange(tests):
    print actions[readkey()]

