#encoding: utf-8
def substitui(lista, tamanho):
    for i in range(0, tamanho):
        if lista[i] < 0:
            lista[i] = 0
        elif lista[i] < 10:
            lista[i] = 1
        else:
            lista[i] = 2
lista = []
tamanho = int(raw_input('Digite o tamanho: '))
for i in range(0, tamanho):
    lista.append(int(raw_input('Digite os valores da lista: ')))
substitui(lista,tamanho)
print lista