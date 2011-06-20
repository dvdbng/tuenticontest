#!/bin/env python
# -*- coding: utf-8 -*-

from PIL import Image

img = Image.open("input-ok")

data = img.getdata()

nimg = Image.new("RGB",(img.size))


#for r in [data[x/3][2-x%3] for x in range(len(data)*3)]:
#for r in open("input-ok").read():

results = []

def asd(i,mode,s,m):
    clean = []
    for r,g,b in list(data)[i:img.size[0]]:
        if mode == 0:
            clean.append(r&1)
        elif mode == 1:
            clean.append(g&1)
        elif mode == 2:
            clean.append(b&1)
        elif mode == 3:
            clean.append((r+g+b)&1)
        elif mode == 4:
            clean.append((r+g)&1)
        elif mode == 5:
            clean.append((r+b)&1)
        elif mode == 6:
            clean.append((g+b)&1)
        elif mode == 7:
            clean.append(r&1)
            clean.append(g&1)
            clean.append(b&1)
        elif mode == 8:
            clean.append(b&1)
            clean.append(g&1)
            clean.append(r&1)

    pos = 0
    val = 0
    cnt = 0
    for bit in clean:
        val += bit<<(s+m*pos)
        pos += 1
        if pos == 8:
            print chr(val),
            if val>48 and val <172:
                cnt+=1
            pos = 0
            val = 0
    print cnt
    #results.append((cnt,s,m,i,mode))


#for s,m in ((7,-1),(0,1)):
#    for i in xrange(30):
#        for mode in xrange(20):
#            asd(i,mode,s,m)

asd(8,8,7,-1)

#results.sort(key=lambda x:x[0])
#print results

#nimg.show()

