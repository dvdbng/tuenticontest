#!/bin/env python


def max_flow(citys,caps,start,end):
    n = len(citys)
    res = {}
    height = {}
    excess = {}
    seen = {}
    for city in citys:
        height[city] = 0
        excess[city] = 0
        seen[city] = 0
        for cityn in citys:
            res[city,cityn] = 0

    list = [city for city in citys if city not in (start,end)]
    def push(u, v):
        send = min(excess[u], caps[u,v] - res[u,v])
        res[u,v] += send
        res[v,u] -= send
        excess[u] -= send
        excess[v] += send

    def relabel(u):
        min_height = float("inf")
        for v in citys:
            if caps[u,v] - res[u,v] > 0:
                min_height = min(min_height, height[v])
                height[u] = min_height + 1

    def discharge(u):
        while excess[u] > 0:
            if seen[u] < n:
                v = citys[seen[u]]
                if caps[u,v] - res[u,v] > 0 and height[u] > height[v]:
                    push(u, v)
                else:
                    seen[u] += 1
            else:
                relabel(u)
                seen[u] = 0

    height[start] = n
    excess[start] = float("inf")
    for city in citys:
        push(start, city)

    p = 0
    while p < len(list):
        u = list[p]
        old_height = height[u]
        discharge(u)
        if height[u] > old_height:
            list.insert(0, list.pop(p))
            p = 0
        else:
            p += 1

    return sum([res[start,x] for x in citys])


import sys
for line in sys.stdin:
    vals = line.split()
    n,start,end = vals[0:3]

    distances = {}
    citys = []
    for distance in vals[3:]:
        o,t,d = distance.split(",")
        distances[(o,t)] = int(d)
        if o not in citys:
            citys.append(o)
        if t not in citys:
            citys.append(t)
    for u in citys:
        for v in citys:
            if (u,v) not in distances:
                distances[u,v]=0

    res = max_flow(citys,distances,start,end)

    print res

