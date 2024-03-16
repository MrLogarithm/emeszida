import sys

from . import EmeszidaParser, EmeszidaTransformer

p = EmeszidaParser
t = EmeszidaTransformer()

path = sys.argv[1]
with open(path) as fp:
    program = fp.read()
    print(program)
    ast = p.parse(program)
    print(ast.pretty())
    program = t.transform(ast)
    program.execute()
