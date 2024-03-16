import sys

from . import EmeszidaParser, EmeszidaTransformer

p = EmeszidaParser
t = EmeszidaTransformer()

path = sys.argv[1]
verbose = "-v" in sys.argv
with open(path) as fp:
    source = fp.read()
    if verbose:
        print(source)
    ast = p.parse(source)
    if verbose:
        print(ast.pretty())
    program = t.transform(ast)
    if verbose:
        program.verbose = True
    program.execute()
