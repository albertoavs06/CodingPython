#encoding: utf-8

a = []
quadrados = []
soma = 0

for i in range(0,4):
    a.append(int(raw_input('Números: ')))
    quadrados.append(a[i]**2)
    soma = soma + quadrados[i]

print a
print quadrados
print soma