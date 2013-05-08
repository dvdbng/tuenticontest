#!/usr/bin/env python
from utils import *
from constraint import *

BiggerConstraint = FunctionConstraint(lambda a,b: a>b )


def formatSol(sol):
    res = [None]*varc
    for var, pos in sol.iteritems():
        res[pos] = var
    return res

n = readint()
for x in xrange(n):
    script = readline()
    parts = re.split('([.<>])', script)
    parts.pop(0)
    assert len(parts)%2 == 0

    scenec = len(parts)/2
    varc = len(set(parts[1::2]))
    domain = range(varc)
    variables = set()
    previousDot = []
    problem = Problem()

    for i in xrange(0, len(parts), 2):
        variable = parts[i+1]
        if variable not in variables:
            problem.addVariable(variable, domain)
            variables.add(variable)
        op = parts[i]
        if op == ".":
            for dot in previousDot:
                problem.addConstraint(BiggerConstraint, [variable, dot])
            previousDot.append(variable)
        elif op == ">":
            assert len(previousDot) > 0
            for dot in previousDot:
                problem.addConstraint(BiggerConstraint, [variable, dot])
        elif op == "<":
            assert len(previousDot) > 0
            problem.addConstraint(BiggerConstraint, [previousDot[-1], variable])


    problem.addConstraint(AllDifferentConstraint(), variables)

    it = problem.getSolutionIter()
    try:
        sol = formatSol(it.next())
    except StopIteration:
        print "invalid"
        continue

    valid = True
    unique = True
    for moresol in it:
        unique = False
        moresol = formatSol(moresol)
        if moresol[0] != sol[0] or moresol[-1] != sol[-1]:
            valid = False
            break
    if unique:
        print ",".join(sol)
    else:
        if valid:
            print "valid"
        else:
            print "invalid"




