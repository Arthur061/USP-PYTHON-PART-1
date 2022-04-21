largura = int(input("Digite a largura: "))
altura = int(input("Digite a altura: "))
str = '#'

def retangulo(largura, altura, str):
    linha_completa = str * largura
    if largura > 2:
        linha_vazia = str + (" " * (largura - 2)) + str
    else:
        linha_vazia = linha_completa
    if altura >= 1:
         print(linha_completa)
    for _ in range(altura - 2):
        print(linha_vazia)
    if altura >= 2:
         print(linha_completa)

retangulo(largura, altura, str)

