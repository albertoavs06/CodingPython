#!/usr/bin/env python
# -*- coding: UTF-8 -*-

print "1 - Soma"
print "2 - Subtraçãoo"
print "3 - Multiplicaçãoo"
print "4 - Divisão"
print "5 - Sair"
opcao = int(raw_input("Escolha uma opção: "))
while opcao != 5 :
    numero1 = int(raw_input("Digite o primeiro número: "))
    numero2 = int(raw_input("Digite o segundo número: "))
    if opcao == 1 :
        print numero1, " + ", numero2, " = ", numero1+numero2
    elif opcao == 2 :
        print numero1, " - ", numero2, " = ", numero1-numero2
    elif opcao == 3 :
        print numero1, " * ", numero2, " = ", numero1*numero2
    elif opcao == 4 :
        print numero1, " / ", numero2, " = ", numero1/numero2
    elif opcao == 5 :
        print "Sair"
    else :
        print "Digite uma op��o v�lida"

    print "1 - Soma"
    print "2 - Subtração"
    print "3 - Multiplicação"
    print "4 - Divisão"
    print "5 - Sair"
    opcao = int(raw_input("Escolha uma opção: "))
    
