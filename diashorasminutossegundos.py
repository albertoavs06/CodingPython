dias = int(input("Digite o n�mero de dias: "))
horas = int(input("Digite o n�mero de horas: "))
minutos = int(input("Digite o n�mero de minutos: "))
segundos = int(input("Digite o n�mero de segundos: "))

horas += dias * 24
minutos += horas * 60
segundos += minutos * 60

print("O tempo total digitado em segundos � %d" %segundos)
