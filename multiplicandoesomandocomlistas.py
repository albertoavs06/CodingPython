#encoding: utf-8

numeros = []
soma = 0
multiplicacao = 1

for i in range(0,5):
    numeros.append(int(raw_input('Informe um número: ')))

for i in numeros:
    soma = soma + i
    multiplicacao = multiplicacao * i

print soma
print multiplicacao