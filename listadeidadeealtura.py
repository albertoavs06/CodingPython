#encoding: utf-8

idade = []
altura = []

for i in range(0, 5):
    idade.append(raw_input('Digite a idade: '))
    altura.append(raw_input('Digite a altura: '))

print altura
print altura[::-1]
print idade
print idade[::-1]