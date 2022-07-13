import sys
import time



def verifica_saida(jogo_velha):
    # sair: determina se ao final da execução dessa função o programa será encerrado.
    sair = False

    # o *desenho* do jogo da velha é separado em linhas, colunas e diagonais, para verificar se foi 
    # feito algum jogo(alguém ganhou*).
    # No jogo da velha, se qualquer fileira, seja na vertical, horizontal ou diagonal estiver preechida
    # com os mesmos símbolos('X' ou 'O'), então alguém ganhou o jogo.

    # Facilitando sua vida...

    # | [0][0] | [0][1] | [0][2] |
    # | [1][0] | [1][1] | [1][2] |
    # | [2][0] | [2][1] | [2][2] |

    linhas = jogo_velha[:]
    colunas = [ [linhas[0][0], linhas[1][0], linhas[2][0]], [linhas[0][1], linhas[1][1], linhas[2][1]], [linhas[0][2], linhas[1][2], linhas[2][2]] ]
    diagonal = [ [linhas[0][0], linhas[1][1], linhas[2][2]], [linhas[0][2], linhas[1][1], linhas[2][0]] ]

    # dict_possibilidades: dicionário que emgloba as linhas, colunas e diagonais, transformando cada
    # uma das listas internas em string(com o método "".join()), para futura verificação com 'xxx' /
    # 'ooo'.

    dict_possibilidades = {   
        'linhas' : ("".join(linhas[0]), "".join(linhas[1]), "".join(linhas[2])),
        'colunas' : ("".join(colunas[0]), "".join(colunas[1]), "".join(colunas[2])),
        'diagonal' : ("".join(diagonal[0]), "".join(diagonal[1]))
    }
    
    # 'X': representa os lances do jogador 1
    simbolo1 = 'X'
    # 'O': representa os lances do jogador 2
    simbolo2 = 'O'
   
    # o laço for vai verificar se 'xxx' ou 'ooo' ocorre na 'linhas', 'colunas', ou 'diagonal', se sim
    # então sair = True

    for chave in dict_possibilidades.keys():
        # Ex.: simbolo1 = 'X' ~> simbolo1 * 3 = 'XXX'
        # Ex.: simbolo2 = 'O' ~> simbolo2 * 3 = 'OOO'

        if (simbolo1 * 3) in dict_possibilidades[chave]:
            print("Jogador 1 venceu!")
            sair = True
            break

        if (simbolo2 * 3) in dict_possibilidades[chave]:
            print("Jogador 2 venceu!")
            sair = True
            break

    return sair



def troca(c, ln, col, simbolo):
    # campo(c) na linha 'ln', coluna 'col', recebe 'simbolo' ('X' ou 'O')
    # Exemplo.:
    # posicao: 5
    # ln(linha) ~> | 4 | 5 | 6 |
    # ln(linha) ~> | 4 | X/O | 6 |

    c[ln][col] = simbolo

    return c 



def verifica_jogada(campo, rodada, lance, marcacao):
    # VARIÁVEIS LOCAIS: 
    # jogo_da_velha ~> campo
    # jogadas ~> rodada
    # posicao ~> lance
    # marcacao ~> marcacao  :\

    # Critério de avaliação:
    # A posição inserida pelo jogador deve ser um inteiro de 1 a 9, e o campo correspondente não pode estar preenchido('X' / 'O').
    # Qualquer outra entrada que vá além da condição acima, não contabiliza a rodada.

    # se lance for um número entre 1 e 9, então o usuário digitou uma posição válida. 
    if (lance in '123456789') and (lance.isdigit()):

        try:
            # Se lance <= '3': o usuário escolheu um campo da terceira linha(debaixo) ~> | 1 | 2 | 3 |
            # Senão se(else if -- elif) lance <= '6': o usuário escolheu um campo da segunda linha(meio) ~> | 4 | 5 | 6 |
            # Senão se(else if -- elif) lance <= '9': o usuário escolheu um campo da primeira linha(de cima) ~> | 7 | 8 | 9 |

            # if ( lance == campo[ linha ][ campo[linha].index(lance) ] )
            # verificamos se o lance(que pode ser um dos números que indica a posição ~> 1 a 9) é
            # igual a algum elemento de sua linha(leia os comentários anteriores), se sim, então aquele
            # "espaço" não foi marcado pelo usuário(ou seja, não tem "X" / "O" ~> portanto, está como 
            # sua formação inicial(jogo_da_velha)).

            # campo = troca(campo, indice(linha), coluna(lista_interna), marcacao)
            # rodada +=1
            # se a condição for verdadeira(ln 87..91), então iremos trocar o número daquele "quadradinho"
            # ..coluna... pelo simbolo do jogador ('X' / 'O'), chamando a função troca.
            
            if (lance <= '3'):
                if (lance == campo[2][campo[2].index(lance)]):
                    campo = troca(campo, 2, campo[2].index(lance), marcacao)
                    rodada += 1
            
            elif (lance <= '6'):
                if (lance == campo[1][campo[1].index(lance)]):
                    campo = troca(campo, 1, campo[1].index(lance), marcacao)
                    rodada += 1

            elif (lance <= '9'):
                if (lance == campo[0][campo[0].index(lance)]):
                    campo = troca(campo, 0, campo[0].index(lance), marcacao)
                    rodada += 1


        # método .index() gera uma exceção do tipo ValueError caso o booleano seja False.
        except ValueError:
            print(f'Posição {lance} já foi marcada.')
    
    else:
        print('- A posição informada está incorreta! - '.upper(), 'Digite um número correspondente aos campos do jogo da velha.')


    # Retorna o campo e a lista, caso foram alteradas, então é atribuido o novo campo e rodada para
    # os parâmetros reais jogo_da_velha e jogadas.
    return campo, rodada



def main():

    print('''\n
    -
    -
    Autor: Matias
    Data: 05 / 06 / 22
    Nome do programa: Jogo da velha
    -
    -
    Atenção ao jogar:
    -
    Em um jogo da velha, cada "quadradinho" corresponde a um campo,
    que será identificado nesse programa por NÚMEROS, de 1 a 9.
    Portanto, se são 9 quadradinhos, teremos 9 rodadas. Cada usuário
    deverá jogar UMA VEZ POR RODADA.
    -
    Se uma opção inválida for inserida incorretamente, a rodada não
    será contabilizada.
    -
    -
    Jogador 1: X
    Jogador 2: 0
    -
    Bom jogo!
    \n
    ''')
    time.sleep(2)

    # criando os campos do jogo da velha
    jogo_da_velha = [list('789'), list('456'), list('123')]

    # jogadas: cada lance de um jogador corresponde a uma jogada.
    jogadas = 1
    
    # jogadas <= 9: o jogo da velha é composto por 9 campos, que devem ser preecnhidos a cada jogada.
    
    while jogadas <= 9:

        print('JOGO DA VELHA  X  /  O')
        print('')

        # exibindo o campo completo
        for linha in jogo_da_velha:
            print('-' * 13)
            print('| {0} | {1} | {2} |'.format("".join(linha[0]), "".join(linha[1]), "".join(linha[2])))

        print('-' * 13)
        print(f'\nRODADA {jogadas}\n')

        marcacao = str()
        jogador = int()

        if (jogadas % 2) == 1:
            jogador = 1
            marcacao = 'X'
        else:
            jogador = 2
            marcacao = 'O'

        # solicitando uma posição para marcar
        posicao = input(f'JOGADOR {jogador} | Insira a posição do campo a marcar(de 1 a 9) ~> ')
        time.sleep(.5)

        # Função verifica_jogada: retorna 2 valores como saída. Sendo o primeiro elemento desempacotado é 
        # o jogo da velha alterado(com a marcação('X' ou 'O') já inclusa), e o segundo elemento corresponde
        # ao número de rodadas(jogadas). A sintaxe do python permite esse tipo de atribuição, visto que o 
        # módulo chamado a seguir retorna dois valores, que serão desempacotados na mesma ordem(left-to-right)
        # que as variáveis anteriores ao sinal de atribuição(nº valores retornados == nº de variáveis que receberam atribuição).

        jogo_da_velha, jogadas = verifica_jogada(jogo_da_velha, jogadas, posicao, marcacao)
        
        print('')

        time.sleep(.5)

        if verifica_saida(jogo_da_velha):
            # do modo que a condição do while está estabelecida, assim que o laço é encerrado, o jogo
            # feito(com uma fileira(na horizontal, vertical ou diagonal) completa('X' ou 'O')) não é 
            # exibido, por isso o jogo da velha é printado novamente.

            print('\nFinal:\n')
            print(f"""\n
            {'-'*13}
            | {jogo_da_velha[0][0]} | {jogo_da_velha[0][1]} | {jogo_da_velha[0][2]} |
            | {jogo_da_velha[1][0]} | {jogo_da_velha[1][1]} | {jogo_da_velha[1][2]} |
            | {jogo_da_velha[2][0]} | {jogo_da_velha[2][1]} | {jogo_da_velha[2][2]} |
            {'-'*13}\n\n
            """)

            time.sleep(5)
            sys.exit()

    print("\nDeu velha!\n")

    return None



if __name__ == '__main__':
    main()

