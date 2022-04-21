def partida():
    print('')
    n = int(input('Quantas peças serão retirada? '))
    m = int(input('Limite de peças por jogada? '))
    x = n + (m + 1)
    primeira_vez_computado = False
    primeira_vez_usuario = False

    if x != 0:
        PcJoga = True
        primeira_vez_computado = True
    else:
        PcJoga = False
        primeira_vez_usuario = True

        while n > 0 :
            if PcJoga == True:
                if primeira_vez_computado == True:
                    print('')
                    print('***** Computador começa *****')
                    print('')
                    primeira_vez_computado = False
                    valor_tirado = computador_escolhe_jogada(m, m)
                    PcJoga = False
                    if valor_tirado == 1:
                        print('O computador tirou 1 peça')
                    else:
                        print('O computador tirou {} peças'.format(valor_tirado))
                else:
                    if primeira_vez_usuario == True:
                        print('')
                        print('***** Voce começa *****')
                        print('')
                        primeira_vez_usuario = False
                        valor_tirado = usuario_escolhe_jogada(n, m)
                        PcJoga = True
                        if valor_tirado == 1:
                            print('')
                            print('Voce retirou 1 peça!')
                        else:
                            print('')
                            print('Voce retirou {} peças!'.format(valor_tirado))
                    n = n - valor_tirado
                    if n > 0:
                        print('Agora restam {} peças'.format(n))
                if PcJoga == True:
                    print('')
                    print('Fim do jogo!! Voce ganhou!!!')
                    print('')
                    return 1
                else:
                    print('')
                    print('Fim do jogo!! O computador ganhou!!!')
                    print('')
                    return 0
def usuario_escolhe_jogada(n, m):
    valor_tirado = 0
    while valor_tirado == 0:
        valor_tirado = int(input('Quantas peças voce vai tirar? '))
        if valor_tirado > n or valor_tirado > m or valor_tirado < 1:
            print('')
            print('Jogada invalida, tente novamente :(')
            print('')
            valor_tirado = 0
            return valor_tirado
def computador_escolhe_jogada(n, m):
    if n <= m:
        return n
    else:
        sobrou = n % (m + 1)
        if sobrou > 0:
            return sobrou
        return m
def campeonato():
    usuario = 0
    computador = 0
    i = 1

    for _ in range(3):
        print('')
        print('***** Rodada {} *****'.format(i))
        id_ganhou = partida()
        i = i + 1
        if id_ganhou == 1:
            usuario = usuario + 1
        else:
            computador = computador + 1
    print('*****Fim do campeonato!*****')
    print('Placar: Voce {} x {} Computador'.format(usuario, computador))
escolha = 0
while escolha == 0:
    print('')
    print('Bem-vindo ao jogo NIM!! Escolha:')
    print('')
    print('1- Para jogar isolado')
    print('2- Para jogar campeonato')
    escolha = int(input())
    if escolha == 1:
        partida()
        break
    elif escolha == 2:
        print('Voce escolheu campeonato!!')
        print('')
        campeonato()
        break
    else:
        print('Número invalido :( Escolha outro número')
        print('')
        escolha = 0