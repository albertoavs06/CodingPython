#encoding: utf-8

valor = float(input('Valor: '))
porcentagem = float(input('Porcentagem: '))

valorDesconto = valor * (porcentagem/100)
valorTotal = valor - valorDesconto

print 'Valor total ', valorTotal