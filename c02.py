#!/bin/env python

import bisect, sys

# a list of cosecutive prims
prims=[]

def is_prim(x):
    last_checked = 2
    for prim in prims:
        last_checked = prim
        if x == prim:
            return True
        elif x % prim == 0:
            return False

    #unknown, slow-check
    for i in range(last_checked+1,x):
        if x % prim == 0:
            return False

    return True


def insert_prime(x):
    if len(prims) == 0 or prims[-1] <x:
        prims.append(x)

def is_eprim_given_is_prime(x):
    rev = int(str(x)[::-1])
    return x != rev and is_prim(rev)

for line in sys.stdin:
    max=int(line)
    for i in range(2,max):
        if is_prim(i):
            insert_prime(i)
    res = 0
    for prim in prims:
        if prim < max and is_eprim_given_is_prime(prim):
            res += prim
    print res
