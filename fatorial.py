def fat(n):
    resultado = 1
    while n > 0:
        resultado = resultado * n
        n = n - 1
    return resultado

# testes
print "Fatorial de 3: ", fat(3)