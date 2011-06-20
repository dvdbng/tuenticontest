#!/bin/env python

import sys
for line in sys.stdin:
    print sum([int(num) for num in line.split()])

