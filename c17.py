#!/bin/env python

from PIL import Image

img = Image.open("input-18")
w,h = img.size
data = img.getdata()
nimg = Image.new("RGB",(img.size))

import sys

colors = {}
for pos in xrange(w):
    if data[pos] not in ((255,0,0),(0,255,0)):
        for i in range(h):
            r,g,b = data[pos+i*w]
            sys.stdout.write(chr(r)+chr(g)+chr(b))


