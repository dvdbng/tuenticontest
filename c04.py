#!/bin/env python



import sys

def filter_index(l,index):
    return [l[x] for x in xrange(len(l)) if x != index]

def nonoptimal_solution(cows,weight_left):
    yescows = []
    nocows = []
    totalmilk = 0
    for cow in cows:
        if cow[2] <= weight_left:
            yescows.append(cow)
            totalmilk += cow[1]
            weight_left -= cow[2]
        else:
            nocows.append(cow)
    return totalmilk,weight_left,yescows,nocows

for line in sys.stdin:
    num,weight_left,cowweight,cowmilk = line.split()
    num = int(num)
    weight_left = int(weight_left)
    cowweight = map(int,cowweight.split(","))
    cowmilk = map(int,cowmilk.split(","))

    basemilk = sum([cowmilk[i] for i in xrange(num) if cowweight[i] == 0])

    cows = [(cowmilk[i]/float(cowweight[i]),cowmilk[i], cowweight[i]) for i in xrange(num) if cowweight[i] > 0]
    cows.sort(key=lambda x: x[0])
    cows.reverse()

    totalmilk,weight_left,yescows,nocows = nonoptimal_solution(cows,weight_left)
    optimal_solution = False
    while weight_left > 0 and not optimal_solution: #solution may be non-optimal
        optimal_solution = True
        for cow in yescows:
            nosol = nonoptimal_solution(nocows,cow[2]+weight_left)
            if nosol[0] > cow[1]:
                yescows = filter(lambda x: x!=cow,yescows)+nosol[2]
                cows.sort(key=lambda x: x[0])
                cows.reverse()
                nocows = filter(lambda x: x not in yescows,cows)
                totalmilk += nosol[0] - cow[1]
                print totalmilk
                weight_left = nosol[1]
                optimal_solution = False

    print totalmilk+basemilk
