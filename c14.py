#!/bin/env python

import sys

for line in sys.stdin:
    line = line.split()
    w,l,n = map(int,line[0:3])
    rects_data = [0,0,w,l,1] + map(int,line[3:])
    rects = []
    colors = {}
    events = []
    for i in range(n+1):
        ax,ay,bx,by,c = rects_data[i*5:i*5+5]
        rect = [ax,ay,bx,by,i+1,c]
        colors[c]=0
        events.append((ax,"S",rect))
        events.append((bx,"E",rect))
        rects.append(rect)

    actuals = []
    events.sort(key=lambda x:x[0])
    for p in xrange(len(events)-1):
        ex,et,er = events[p]
        fx = events[p+1][0]

        if et == "S":
            actuals.append(er)
        else:
            actuals.remove(er)

        eventsy = []
        for rect in actuals:
            eventsy.append((rect[1],"S",rect))
            eventsy.append((rect[3],"E",rect))

        eventsy.sort(key=lambda x:x[0])

        actualsy = []
        for py in xrange(len(eventsy)-1):
            ey,ety,ery = eventsy[py]
            fy = eventsy[py+1][0]
            if ety == "S":
                actualsy.append(ery)
            else:
                actualsy.remove(ery)

            winner = max(actualsy,key=lambda x:x[4])
            colors[winner[5]] += (fx-ex)*(fy-ey)

    colors = filter(lambda x:x[1]>0,colors.items())
    colors.sort(key=lambda x:x[0])
    print " ".join([str(colors[i/2][i%2]) for i in xrange(len(colors)*2)])

