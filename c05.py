#!/bin/env python

digits = {
    '0':6,
    '1':2,
    '2':5,
    '3':5,
    '4':4,
    '5':5,
    '6':6,
    '7':3,
    '8':7,
    '9':6,
}

def leds(time):
    return sum([digits[i] for i in time])

def pad(x):
    return ("0"+str(x))[-2:]

def seconds_to_time(seconds):
    return pad(((seconds/3600)%24))+pad(((seconds/60)%60))+pad((seconds%60))

def total(seconds):
    tot = 0
    for i in xrange(seconds):
        tot += leds(seconds_to_time(i))

    tot += leds(seconds_to_time(seconds))
    return tot

import sys
for line in sys.stdin:
    print total(int(line))

