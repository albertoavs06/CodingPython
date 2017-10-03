#encoding: utf-8

#Declarando a função
def sequencia(valor):
    for i in range(1, valor + 1):
        for j in range(1, i + 1):
            print j,
        print

#Código principal

valor = int(raw_input('Valor: '))
sequencia(valor)