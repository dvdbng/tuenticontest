#!/usr/bin/env python
from utils import *

def solve_case(case):
    budget = readint()
    prices = readints()

    prices_clean = [prices[0]]

    for price in prices:
        if price == prices_clean[-1]:
            continue

        if len(prices_clean) >= 2 and (
                (price > prices_clean[-1] > prices_clean[-2]) or
                (price < prices_clean[-1] < prices_clean[-2])
            ):
            prices_clean.pop()

        prices_clean.append(price)

    if len(prices_clean) >= 2 and prices_clean[0] > prices_clean[1]:
        prices_clean.pop(0)

    if len(prices_clean) >= 2 and prices_clean[-1] < prices_clean[-2]:
        prices_clean.pop()

    assert len(prices_clean)%2 == 0

    total = float(budget)
    for i in xrange(0,len(prices_clean), 2):
        total = (total / prices_clean[i])*prices_clean[i+1]

    print int(total)


for case in xrange(readint()):
    solve_case(case)

