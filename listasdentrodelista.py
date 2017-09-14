#encoding: utf-8

lista1 = []
lista2 = []
lista3 = []

print 'Digite os números da primeira lista'
for i in range(0, 5):
    lista1.append(int(raw_input('Informe um numero: ')))

print 'Digite os números da segunda lista'
for i in range(0, 5):
    lista2.append(int(raw_input('Informe um numero: ')))

for i in range(0, 5):
    lista3.append(lista1[i])
    lista3.append(lista2[i])
print lista3