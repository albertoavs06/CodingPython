nome = raw_input('Digite um nome: ')
while len(nome) <= 3:
    nome = raw_input("digite seu nome: ")
 
idade = input('Digite sua idade: ')
while idade < 0 or idade > 150:
    idade = input("digite sua idade: ")
 
salario = input('Digite seu salário: ')
while salario <= 0:
    salario = input("digite seu salario: ")
 
sexo = raw_input('Digite seu sexo: ')
while sexo != "f" and sexo != "m":
    sexo = raw_input("digite seu sexo m - masculino ou f - feminino: ")
 
estadoCivil = raw_input('Digite seu estado civil: ')
while estadoCivil != "s" and estadoCivil != "c" and estadoCivil != "v" and estadoCivil != "d":
    estadoCivil = raw_input("digite seu estado civil s - solteiro, c - casado, v - viuvo ou d = divorciado: ")
