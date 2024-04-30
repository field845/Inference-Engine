from collections import defaultdict
from cnf import *
from expr import *

symbols = set()


def pl_fc_entails(kb, q):
    """
    [Figure 7.15]
    Use forward chaining to see if a PropDefiniteKB entails symbol q.
    >>> pl_fc_entails(horn_clauses_KB, expr('Q'))
    True
    """
    count = {c: len(conjuncts(c.args[0])) for c in kb.clauses if c.op == '==>'}
    inferred = defaultdict(bool)
    agenda = [s for s in kb.clauses if is_prop_symbol(s.op)]
    for item in agenda:
        symbols.add(item)

    while agenda:
        print(agenda)
        p = agenda.pop()
        if p == q:
            return True
        if not inferred[p]:
            inferred[p] = True
            symbols.add(p)
            print(kb.clauses_with_premise(p))
            for c in kb.clauses_with_premise(p):
                count[c] -= 1
                print(c)
                if count[c] == 0:
                    agenda.append(c.args[1])

    return False


def get_fc_symbols():
    return symbols