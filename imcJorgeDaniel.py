print"vamos calcular o seu imc       por daniel\o/ jorge"
altura=float(input("digite sua altura"))
peso=float(input("digite seu peso"))
imc=(peso)/(altura**2)
if imc <17:
    print " voce e muito magro(a) esta abaixo do peso seu palito",imc
elif imc>=17 and imc<=18.49:
    print "voce esta magro(a)",imc
elif imc>=18.5 and imc<=24.99:
    print "parabens seu peso esta ideal para sua altura \o/ \o/",imc
elif imc>=25 and imc<=29.99:
    print "voce esta como a prof e esta gorda",imc
elif imc>=30 and imc<=34.99:
    print"cuidado seu gordo feio",imc
elif imc>=35 and imc<=39.99:
    print "pare de comer ;-;  ",imc
else:
    print "voce daqui a pouco morrera, obeso grau 3",imc
    
            
