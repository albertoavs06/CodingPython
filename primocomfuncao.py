#encoding: utf-8

#Função para saber se o número digitado é primo
def primo(numero):
    contador = 1
    for i in range(2, numero): #ele começa o loop do número 2 pq qq número é divisível por 1
        if numero % i == 0: #verifica se o número digitado é divisível pelo valor de i
            contador+=1
    if contador != 1: #se ele tiver mais de um divisor é primo
        print 'O número ', numero, ' não é primo'
    else: #se ele tiver só um divisor ele é primo
        print 'O número ', numero, ' é primo'

numero = int(raw_input('Digite um número: '))
primo(numero)