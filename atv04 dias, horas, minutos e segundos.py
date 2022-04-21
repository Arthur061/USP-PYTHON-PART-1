segundos = int(input('Por favor, entre com o número de segundos que deseja converter: '))
a = segundos // 86400
restante_dias = segundos % 86400
b = restante_dias // 3600
restante_horas = restante_dias % 3600
c = restante_horas // 60
d = restante_horas % 60
print(a,'dias,', b, 'horas,', c, 'minutos e', d, 'segundos.')