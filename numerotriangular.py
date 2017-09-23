#encoding: utf-8

numero = int(input('Entre com o número: '))
i = 1
t = 0
while t < numero:
	t = i*(i+1)*(i+2)
	i += 1

if t == numero:
	print ('%d é triangular' %numero)
else:
	print ('%d não é triangular' %numero)