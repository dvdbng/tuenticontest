#!/bin/env python

STARDATE_STAR = 25000

def minimal_distance(num,distances,start,end):

    data = {}

    for planet in range(num+1):
        data[planet] = (float("inf"),None)

    data[start] = (STARDATE_STAR,None)

    for i in xrange(1,num+1):
        for u,v in distances:
            if data[u][0] + distances[(u,v)] < data[v][0]:
                data[v] = (data[u][0]+distances[(u,v)],u)

    for u,v in distances:
       if data[u][0] + distances[(u,v)] < data[v][0]:
           # negative-weight cicle:
           # 1.- Go throught the cicle
           # 2.- Find past you
           # 3.- Repeat 1 and 2
           # 4.- ?????
           # 5.- Profit!
           return "BAZINGA"

    dist=data[end][0]

    if dist == float("inf"):
       return "BAZINGA"
    return dist

import sys
for line in sys.stdin:
    vals = line.split()
    num,earth,target = map(int,vals[0:3])

    distances = {}
    for distance in vals[3:]:
        o,t,d = map(int,distance.split(","))
        distances[(o,t)] = d


    res = minimal_distance(num,distances,earth,target)

    print res

