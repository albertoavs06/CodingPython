raio = float(input("Digite o raio do cilindro: "))
altura = float(input("Digite a altura do cilindro: "))

PI = 3.14
DOIS = 2

area = DOIS * PI * raio * (raio + altura)
volume = PI * (raio * DOIS) * altura

print "A �rea do cilindro � ", area, " e o volume � ", volume
