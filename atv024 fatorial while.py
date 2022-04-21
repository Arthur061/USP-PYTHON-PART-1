from math import factorial
n = 1
while n > 0:
    n = int(input('Digite um número inteiro positivo que deseja fatoriar: '))
    if n < 0:
        #print('Zero fatorial vale 1')
        print('Por favor, o número tem que ser maior que zero :)')
        #n = 0
    while n >= 0:
        if n >= 0:
            fatorial = factorial(n)
            print('O número {} tem o fatorial igual a {}'.format(n, fatorial))
            break

