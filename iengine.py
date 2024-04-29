import sys
from data_convertor import *
from entail_engine import *
from fc import *
from bc import *
from PropDefiniteKB import *
from expr import *

file_name, p, q = data_convertor()
method = sys.argv[2]

definite_clauses_KB = PropDefiniteKB()
for clause in p:
    definite_clauses_KB.tell(expr(clause))


def switch(method):  # to switch between different search algorithms
    if method.lower() == "tt":
        return tt_entails(p, q)
    elif method.lower() == "fc":
        result = pl_fc_entails(definite_clauses_KB, expr(q))
        symbols = get_fc_symbols()
        return result, symbols
    elif method.lower() == "bc":
        result = pl_bc_entails(definite_clauses_KB, expr(q))
        symbols = get_bc_symbols()
        return result, symbols
    else:
        print("Invalid method")


def main():
    result, symbols = switch(method)
    if len(sys.argv) < 3:
        print("Please Enter Correct Argument")
    if result:
        symbol_str = ', '.join(str(symbol) for symbol in symbols)
        print("YES: " + symbol_str)
    else:
        print("NO")


main()
