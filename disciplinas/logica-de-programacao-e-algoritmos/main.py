import jogo as j
import fileHandler as fh

def mostrar_menu():
    print('='*30)
    print(' '*7 + 'JOGO DA FORCA')
    print('='*30)
    print('\n1 - JOGAR')
    print('2 - SCORE')
    print('3 - SAIR\n')
    print('='*30)

arquivo = 'score.txt'
if fh.existeArquivo(arquivo):
    print('Arquivo localizado no computador.')
else:
    print('ARQUIVO NÃO EXISTE.')
    fh.criaArquivo(arquivo)

while True:
    mostrar_menu()
    opcao = int(input('Escolha a opção (1/2/3): '))

    if opcao == 1:
        print('Iniciar jogo!')
        j.jogar()
    elif opcao == 2:
        print('SCORE')
        dados = fh.listarArquivo('score.txt')
        if not dados:
            print('Score vazio.')
        else:
            i = 1
            for jogador in dados:
                print(f'{i} -> {jogador[0]}, Pontuação: {jogador[1][:-1]}')
                i += 1               

    elif opcao == 3:
        print('Saindo do jogo. Até mais.')
        break
    else:
        print('Opção inválida. Tente outra.')