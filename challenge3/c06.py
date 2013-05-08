#!/usr/bin/env python

from utils import *
import heapq

moves = set(range(4))
deltas = [(0,-1),(-1,0),(0,1),(1,0)]

def distance(pos1, pos2):
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

def bound(pos, goal, speed, stop):
    time = distance(pos, goal)/speed
    if pos[0] != goal[0] and pos[1] != goal[1]:
        time += stop
    return time

def newpos(M, oldpos, move):
    dx,dy = deltas[move]
    nx,ny = oldpos
    time = 0
    while M[nx+dx, ny+dy] == ".":
        time += 1
        nx += dx
        ny += dy
    if M[nx+dx, ny+dy] == "O":
        time += 1
        nx += dx
        ny += dy
    return (nx,ny), time

def valid_moves(M, pos):
    res = set()
    for move in moves:
        dx,dy = deltas[move]
        if M[pos[0] + dx, pos[1] + dy] in (".", "O"):
            res.add(move)
    return res


def purge_heap(heap, limit):
    s=len(heap)
    heap = filter(lambda x: x[0] < limit, heap)
    heapq.heapify(heap)
    e=len(heap)
    #if e<s:
    #    print "pruned", (s-e), "branches"
    return heap

def replace_solution(heap, pos, newbound, newtime):
    for i in xrange(len(heap)):
        if heap[i][1] == pos:
            heap[i] = (newbound, pos, newtime)
    heapq.heapify(heap)

def solve(M, pos, size, goal, speed, delay):
    upper_bound = 1<<31
    solutions = [(bound(pos, goal, speed, delay), pos, 0)] # Min-heap with the solutions to explore
    sols_time = {pos: 0} # Map of the subproblems to explore, to make sure we don't explore the same subproblem twice

    while len(solutions):
        bnd, pos, time = heapq.heappop(solutions)
        if M[pos] == "O":
            #print "sol found", pos, time
            if time < upper_bound:
                upper_bound = time
                heap = purge_heap(solutions, upper_bound)
        else:
            for move in valid_moves(M, pos):
                npos, desp = newpos(M, pos, move)
                nbound = time + delay + desp/speed + bound(npos, goal, speed, delay)
                #print "expand", pos, move, nbound
                if nbound < upper_bound:
                    ntime = time + delay + desp/speed
                    if npos in sols_time:
                        if sols_time[npos] > ntime: # Better solution, replace
                            sols_time[npos] = ntime
                            replace_solution(solutions, npos, nbound, ntime)
                    else:
                        heapq.heappush(solutions, (nbound, npos, ntime))
                        sols_time[npos] = ntime

    return int(round(upper_bound))

for x in xrange(readint()):
    w,h,speed,time = readints()
    M = {}
    goal = None
    start = None
    for y in xrange(h):
        line = readline().decode("utf-8")
        for x in xrange(w):
            if line[x] == "O":
                goal = x,y
                M[x,y] = "O"
            elif line[x] == "X":
                start = x,y
                M[x,y] = "."
            elif line[x] == "#":
                M[x,y] = "#"
            else: # Too busy to set the encoding of the file..!
                M[x,y] = "."

    #print goal, start

    print solve(M, start, (w,h), goal, float(speed), time)

