raio = float(input("Digite o raio do cilindro: "))
altura = float(input("Digite a altura do cilindro: "))

PI = 3.14
DOIS = 2

area = DOIS * PI * raio * (raio + altura)
volume = PI * (raio * DOIS) * altura

print "A área do cilindro é ", area, " e o volume é ", volume
