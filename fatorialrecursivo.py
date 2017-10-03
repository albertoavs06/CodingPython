#encoding: utf-8

def fatorialRecursivo(n):
    if n == 0:
        return 1
    else:
        return n * fatorialRecursivo(n-1)

# testes
print "Fatorial de 5: ", fatorialRecursivo(5)






















