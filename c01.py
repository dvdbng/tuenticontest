#!/bin/env python

import re, sys

def times(a):
    res=1
    for x in a:
        res = res*x
    return res

class TuentiExpression():
    tokens = [
        ('EXP_START', r'\^(=|#|@)'),
        ('EXP_END', r'\$'),
        ('LITERAL', r'\d+'),
    ]
    operators = {
        "=": lambda *a: sum(a),
        "#": lambda *a: times(a),
        "@": lambda a,b=None: -a if b is None else a-b,
    }
    token_regex = re.compile('|'.join('(?P<%s>%s)' % pair for pair in tokens))
    whitespace_regexp = re.compile('\s*')
    def __init__(self,s,pos=0):
        self.pos = pos
        self.consume_whitespace(s)
        tk = self.token_regex.match(s,self.pos)
        assert tk is not None #check for sintax errors

        type = tk.lastgroup
        self.pos += len(tk.group(type))

        if type == "LITERAL":
            self.type = "LITERAL"
            self.value = int(tk.group(type))
        elif type == "EXP_START":
            self.type = "EXP"
            self.operator = tk.group(type)[1:]
            self.args = []

            #maybe do-while loops aren't a bad idea, after all
            while True:
                expr = TuentiExpression(s,self.pos)
                self.pos = expr.pos
                if expr.type == "EXP_END":
                    break
                self.args += [expr]

        elif type == "EXP_END":
            self.type = "EXP_END"
        else:
            raise "Syntax error"

    def execute(self):
        if self.type == "LITERAL":
            return self.value
        elif self.type == "EXP":
            return self.operators[self.operator](*[arg.execute() for arg in self.args])

    def consume_whitespace(self,s):
        # since whitespace_regexp can match a empty string,
        # whitespace_regexp.match will allways return a match object
        self.pos += len(self.whitespace_regexp.match(s,self.pos).group(0))

for line in sys.stdin:
    print TuentiExpression(line).execute()
