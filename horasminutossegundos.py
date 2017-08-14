s = int(input("Digite os segundos "))

h = s // 3600
seg_restante = s % 3600
m = seg_restante // 60
seg_restante_final = seg_restante % 60

print(h, " horas ", m, " minutos ", seg_restante_final, "segundos")
