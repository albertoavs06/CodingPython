#encoding: utf-8

import math

def valor(x):
    if x == 1 or x == 2 or x == 3:
        return x**2
    elif x == 4 or x == 9:
        return math.sqrt(x)
    elif x == 6 or x == 7 or x == 8:
        return x / 2
    else:
        return 'Opção inválida'

x = float(raw_input('Digite o valor de x: '))
print valor(x)