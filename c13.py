#!/bin/env python

from PIL import Image
import sys

img = Image.open("trabaja.bmp")
imgdata = img.getdata()
imgw,imgh = img.size

for line in sys.stdin:
    component = "RGB".index(line[0])
    y = int(line[1:])
    total = 1
    for i in xrange(y*imgw,(y+1)*imgw):
        total += imgdata[i][component]
    print total



