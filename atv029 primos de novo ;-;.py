def primo(x):
    fator = 2
    while (x % fator != 0) and (fator <= x / 2):
        fator = fator + 1
    if (x % fator != 0) or (x == 2):
        return True
    else:
        return False

def n_primos(x):
    i = 2
    conta = 0
    fator = 2
    while(i <= x):
        if(primo(i)):
            conta = conta +1
        i = i + 1
    return conta