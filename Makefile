test:
	python -m unittest

interpret:
	@python -c "import emeszidap = emeszida.EmeszidaParsert = emeszida.EmeszidaTransformer()while True:  parse = p.parse(input('> '))  print('Parse tree:', parse, '\n')  value = t.transform(parse)  print('AST:', value, '\n')"

.PHONY: test
