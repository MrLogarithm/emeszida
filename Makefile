test:
	python -m unittest

interpret:
	@python -c "import readlineimport emeszidap = emeszida.EmeszidaParsert = emeszida.EmeszidaTransformer()while True:  try:    parse = p.parse(input('> '))    print('Parse tree:', parse.pretty(), '\n')    value = t.transform(parse)    print('AST:', value, '\n')  except Exception as e:    print('Error:', e)"

.PHONY: test
