import sys, math

# Symport type of rule
IN = 0
OUT = 1

objs = { 'in' : IN, 'out' : OUT }

# Types of block
SYM = 1
CRE = 2

# MAX_INT = math.log2(sys.maxsize * 2 + 2)
MAX_INT = sys.maxsize * 2 + 2

def membrane_idents():
    i = 0
    while True:
        yield i
        i += 1

def rule_idents():
    i = 0
    while True:
        yield i
        i += 1

next_membrane_ident = membrane_idents()
next_rule_ident = rule_idents()
