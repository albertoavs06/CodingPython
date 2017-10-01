#encoding: utf-8

lista = []
par = []
impar = []

print 'Digite os números da primeira lista'
for i in range(0, 5):
    lista.append(int(raw_input('Informe um numero: ')))

for i in range(0, 5):
    if lista[i] % 2 == 0:
        par.append(lista[i])
    else:
        impar.append(lista[i])

print lista
print par
print impar
