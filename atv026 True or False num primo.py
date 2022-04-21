def éPrimo(x):
    fator = 2
    while x % 2 != 0 and fator < x/2:
        fator= fator + 1
        if x % fator == 0:
            return False
        else:
            return True

n = int(input('Digite um número inteiro: '))

while n > 0:
    if éPrimo(n):
        print('{} é primo'.format(n))
        n = 0
        break
    else:
        print('{} não é primo :('.format(n))
    n = int(input('Digite um número inteiro: '))
