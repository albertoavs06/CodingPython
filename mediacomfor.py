soma = 0
media = 0
for i in range(4):
    nota[i]=float(input('Nota '))
    soma = soma + nota[i]
media = soma / 4
print 'A média do aluno é: ', media
