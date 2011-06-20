#!/bin/env python


digits = {
    '0':(1,3,4,5,6,7),
    '1':(6,7),
    '2':(1,2,3,5,6),
    '3':(1,2,3,6,7),
    '4':(2,4,6,7),
    '5':(1,2,3,4,7),
    '6':(1,2,3,4,5,7),
    '7':(1,6,7),
    '8':(1,2,3,4,5,6,7),
    '9':(1,2,3,4,5,7),
}

def leds(fromtime,totime):
    diff = [(fromtime[x],totime[x]) for x in range(len(fromtime)) if fromtime[x]!=totime[x]]
    total = 0
    for fromd,tod in diff:
        total += len([1 for led in digits[tod] if led not in digits[fromd]])
    return total

def pad(x):
    return ("0"+str(x))[-2:]

def seconds_to_time(seconds):
    return pad(((seconds/3600)%24))+pad(((seconds/60)%60))+pad((seconds%60))

def total(seconds):
    tot = 36
    for i in xrange(1,seconds+1):
        tot += leds(seconds_to_time(i-1),seconds_to_time(i))

    return tot

import sys
for line in sys.stdin:
    print total(int(line))

