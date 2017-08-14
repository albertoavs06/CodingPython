dias = int(input("Digite o número de dias: "))
horas = int(input("Digite o número de horas: "))
minutos = int(input("Digite o número de minutos: "))
segundos = int(input("Digite o número de segundos: "))

horas += dias * 24
minutos += horas * 60
segundos += minutos * 60

print("O tempo total digitado em segundos é %d" %segundos)
