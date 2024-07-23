# Funções

def cadastrar_livro(id):
    # Opção 1 escolhida
    print(traco * 50)
    print(traco * 10, 'MENU CADASTRAR LIVRO', traco * 18)
    print(f'Id do livro: {id}')
    dic_cadastro = {}
    dic_cadastro['id'] = id
    dic_cadastro['nome'] = input('Por favor entre com o nome do livro: ')
    dic_cadastro['autor'] = input('Por favor entre com o autor do livro: ')
    dic_cadastro['editora'] = input('Por favor entre com a editora do livro: ')
    print(f'{traco * 50}\n')
    
    lista_livro.append(dic_cadastro.copy())

def consultar_livro():
    # Opção 2 escolhida
    while True:
        print(traco * 50)
        print(traco * 10, 'MENU CONSULTAR LIVRO', traco * 18)

        print('Escolha a opção desejada:')
        print('1 - Consultar todos os livros\n2 - Consultar Livro por id')
        print('3 - Consultar Livro(s) por autor\n4 - Retornar')
        op2 = int(input('>>'))       

        if op2 == 1:
            # Consulta todos os livros
            print(traco * 16)
            for livro in lista_livro:   
                print(f'id: {livro['id']}\nnome: {livro['nome']}')
                print(f'autor: {livro['autor']}\neditora: {livro['editora']}\n')

        elif op2 == 2:
            # Consulta livro por id
            consulta_id = int(input('Digite o id do livro: '))
            print(traco * 16)

            livro_id = lista_livro[consulta_id - 1]
            print(f'id: {livro_id['id']}\nnome: {livro_id['nome']}')
            print(f'autor: {livro_id['autor']}\neditora: {livro_id['editora']}\n')

            
        elif op2 == 3:
            # Consulta livro por autor
            consulta_autor = input('Digite o autor do(s) livro(s): ')
            print(traco * 16)

            for livro in lista_livro:
                if livro['autor'] == consulta_autor:
                    print(f'id: {livro['id']}\nnome: {livro['nome']}')
                    print(f'autor: {livro['autor']}\neditora: {livro['editora']}\n') 
            
        elif op2 == 4:
            # Retorna para o menu principal
            break 
        else:
            print('Opção inválida\n') 
            continue

        print(f'{traco * 16}\n{traco * 50}\n')

def remover_livro():
    # Opção 3 escolhida
    print(traco * 50)
    print(traco * 10, 'MENU REMOVER LIVRO', traco * 18)
    id = int(input('Digite o id do livro a ser removido: '))
    del lista_livro[id - 1]
    print('Livro removido com sucesso!')

# Programa principal
print('Bem vindo a Livraria da Pietra Ataulo')
lista_livro = []
id_global = 0
while True:
    traco = '-'
    print(traco * 50)
    print(traco * 15, 'MENU PRINCIPAL', traco * 19)
    print('Escolha a opção desejada:')
    print('1 - Cadastrar Livro\n2 - Consultar Livro(s)\n3 - Remover Livro\n4 - Sair')
    op = int(input('>>'))
    
    if op == 1:
        id_global += 1
        cadastrar_livro(id_global)
    elif op == 2:
        consultar_livro()
    elif op == 3:
        remover_livro()
    elif op == 4:
        print('Encerrando o programa...')
        break 
    else:
        print('Opção inválida\n') 
        continue
