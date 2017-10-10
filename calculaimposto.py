#encoding: utf-8

def somaimposta(taxaimposto, custo):
    return (custo * (taxaimposto / 100)) + custo

taxaimposto = float(raw_input('Taxa: '))
custo = float(raw_input('Custo: '))
print somaimposta(taxaimposto, custo)