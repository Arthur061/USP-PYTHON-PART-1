from math import sqrt
x1 = int(input('Primeira coordenada: '))
y1 = int(input('Segunda coordenada: '))
x2 = int(input('Terceira coordenada: '))
y2 = int(input('Quarta coordenada: '))

print('Ponto A, x = {} e y = {}'.format(x1, y1))
print('Ponto B, x = {} e y = {}'.format(x2, y2))

distancia = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

if distancia >= 10:
    print('longe')
else:
    print('perto')