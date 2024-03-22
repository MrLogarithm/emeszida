test:
	python -m unittest

interpret:
	@python -c "import readlineimport emeszidap = emeszida.EmeszidaParsert = emeszida.EmeszidaTransformer()while True:  try:    parse = p.parse(input('> '))    print('Parse tree:', parse.pretty(), '\n')    value = t.transform(parse)    print('AST:', value, '\n')  except Exception as e:    print('Error:', e)"

paper:
	cd sigbovik; lualatex paper.tex; bibtex paper.aux; lualatex paper.tex; lualatex paper.tex 

.PHONY: test paper
