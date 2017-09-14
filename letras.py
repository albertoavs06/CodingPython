#encoding: utf-8

letras = []
vogais = ['A', 'E', 'I', 'O', 'U']

for i in range(0,10):
    letras.append(raw_input('Digite uma letra: ').upper())

totalConsoantes = 0
consoantes = []

for i in range(0,10):
    if letras[i] not in vogais:
        totalConsoantes+=1
        consoantes.append(letras[i])

print 'Total de consoantes digitadas: ', totalConsoantes
print consoantes

