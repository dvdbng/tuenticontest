#!/usr/bin/env python

from utils import *
import heapq

UP = 0
LEFT = 1
DOWN = 2
RIGHT = 3
NO_MOVE = 4 # To represent the initial movement
moves = set(range(4))
deltas = [(0,-1),(-1,0),(0,1),(1,0)]
oposites = {
    UP: DOWN,
    DOWN: UP,
    LEFT: RIGHT,
    RIGHT: LEFT,
    NO_MOVE: NO_MOVE
}

def distance(pos1, pos2):
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

def newpos(oldpos, move):
    dx,dy = deltas[move]
    return (oldpos[0]+dx, oldpos[1]+dy)

def bound(pos, gems, time):
    cnt = {1:0, 2:0, 5:0}
    for gemp, gemv in gems.iteritems():
        if distance(pos,gemp) <= time:
            cnt[gemv] += 1
    act = 0
    if pos in gems:
        act = gems[pos]
        cnt[act] -= 1

    res_5 = min(cnt[5],time)
    time -= res_5
    res_2 = min(cnt[2],time)
    time -= res_2
    res_1 = min(cnt[1],time)
    time -= res_1
    return res_5*5 + res_2*2 + res_1 + act

def valid_moves(pos, size, lastMove):
    invalid_moves = set((oposites[lastMove],))

    if pos[0] == 0:
        invalid_moves.add(LEFT)
    if pos[0] == size[0]-1:
        invalid_moves.add(RIGHT)
    if pos[1] == 0:
        invalid_moves.add(UP)
    if pos[1] == size[1]-1:
        invalid_moves.add(DOWN)

    return moves.difference(invalid_moves)

def purge_heap(heap, limit):
    s=len(heap)
    heap = filter(lambda x: (-x[0]) > limit, heap)
    heapq.heapify(heap)
    e=len(heap)
    #if e<s:
    #    print "pruned", (s-e), "branches"
    return heap

def solve(gems, pos, size, time, lastMove):
    upper_bound = 0
    tact = ()
    solutions = [(-bound(pos, gems, time), gems, pos, time, lastMove, 0)] # Max-heap with the solutions to explore

    while len(solutions):
        bnd, gems, pos, time, lastMove, val = heapq.heappop(solutions)
        if pos in gems:
            gems = gems.copy()
            val += gems.pop(pos)
        if time == 0:
            #print "sol found", val
            if val > upper_bound:
                upper_bound = val
                heap = purge_heap(solutions, upper_bound)
        else:
            for move in valid_moves(pos, size, lastMove):
                npos = newpos(pos, move)
                nbound = val + bound(npos, gems, time-1)
                #print "expand", pos, move, nbound
                if nbound > upper_bound:
                    heapq.heappush(solutions, (-nbound, gems, npos, time-1, move, val))

    #print tact
    return upper_bound

for x in xrange(readint()):
    size = readints(",")
    ix, iy = readints(",")
    time = readint()
    readint()
    gems = map(lambda x: map(int, x.split(",")), readline().split("#"))
    initial_pos = ix,iy

    # With the problem constrainst, there can be a maximum of 1600 gems we can reach
    interesting_gems = filter(lambda gem: distance(initial_pos, gem) <= time, gems)

    gem_map = {}
    for x,y,v in interesting_gems:
        gem_map[x,y] = v
    print solve(gem_map, initial_pos, size, time, NO_MOVE)

