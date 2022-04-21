#import pytest as pytes
import math

def delta(a, b, c):
    return b ** 2 -4 * a * c

def principal():

    a = float(input('Digite o valor de a: '))
    b = float(input('Digite o valor de b: '))
    c = float(input('Digite o valor de c: '))
    imprime_raizes(a, b, c)

def imprime_raizes(a, b, c):
    d = delta(a, b, c)
    if d == 0:
        raiz1 = ( -b + math.sqrt(d)) / (2 * a)
        print('A única raiz é {:.2f}'.format(raiz1))

    elif d < 0:
        print('Essa equação não possui raizes reais')

    elif d > 0:
        raiz1 = (-b + math.sqrt(d)) / (2 * a)
        raiz2 = (-b - math.sqrt(d)) / (2 * a)
        print('A primeira raiz é {:.2f}'.format(raiz1))
        print('A segunda raiz é {:.2f}'.format(raiz2))

