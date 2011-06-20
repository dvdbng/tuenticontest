#!/bin/env python

tasks = {}

data=open("in","rb")
size = None
reading_tasks = True

class Task():
    def __init__(self,t):
        self.time = t
        self.deps = None
    def set_dependeicies(self, deps):
        self.deps = deps
    def duration(self):
        if self.deps:
            return self.time + max([tasks[task].duration() for task in self.deps])

for line in data:
    if line[0] == "#":
        if size is not None and len(tasks) > 0:
            reading_tasks = False
    elif line != "\n": #ignore blank lines
        if size is None:
            size = int(line)
        else:
            if reading_tasks:
                task,duration = map(int,line.split(","))
                tasks[task] = Task(duration)
            else:
                vals = map(int,line.split(","))
                tasks[vals[0]].set_dependeicies(vals[1:])



import sys

sys.setrecursionlimit(10000) # My laptop hates you
for line in sys.stdin:
    for task in map(int,line.split(",")):
        time = tasks[task].duration()
        print "%s %s" % (task,time)

