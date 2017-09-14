# encoding: utf-8

notas = []
soma = 0
media = 0

for i in range(0,4):
    notas.append(float(raw_input('Digite as notas: ')))
    soma = soma + notas[i]

print notas
media = soma / 4
print 'A média é ', media