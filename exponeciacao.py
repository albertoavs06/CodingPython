base = input("Digite a base: ")
expoente = input("Digite o expoente: ")
baseCalc = 1
i = 0
while i < expoente:
    baseCalc = baseCalc*base
    i = i + 1
print base," ^ ",expoente," = ",baseCalc
