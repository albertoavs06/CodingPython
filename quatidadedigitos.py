#encoding: utf-8

def contadordigitos(n):
    a = str(n)
    return len(a)

n = int(raw_input('N: '))
print contadordigitos(n)