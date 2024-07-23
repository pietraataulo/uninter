# Funções
def cadastrar_livro(id):
    # Opção 1 escolhida
    print("-" * 50)
    print("-" * 10, 'MENU CADASTRAR LIVRO', "-" * 18)
    print(f'Id do livro: {id}')
    dic_cadastro = {'id': id, 'nome': input('Por favor entre com o nome do livro: '),
                    'autor': input('Por favor entre com o autor do livro: ').upper(),
                    'editora': input('Por favor entre com a editora do livro: ')}
    print(f'{"-" * 50}\n')
    lista_livro.append(dic_cadastro.copy())


def consultar_livro():
    # Opção 2 escolhida
    while True:
        try:
            print("-" * 50)
            print("-" * 10, 'MENU CONSULTAR LIVRO', "-" * 18)
            print('Escolha a opção desejada:')
            print('1 - Consultar todos os livros\n2 - Consultar Livro por id')
            print('3 - Consultar Livro(s) por autor\n4 - Retornar')
            op2 = int(input('>>'))
            if op2 == 1:
                # Consulta todos os livros
                print("-" * 16)
                for livro in lista_livro:
                    print(f'id: {livro["id"]}\nnome: {livro["nome"]}')
                    print(f'autor: {livro["autor"]}\neditora: {livro["editora"]}\n')
            elif op2 == 2:
                # Consulta livro por id
                consulta_id = int(input('Digite o id do livro: '))
                print("-" * 16)
                conta_id = False
                for livro in lista_livro:
                    if livro['id'] == consulta_id:
                        conta_id = True
                        print(f'id: {livro["id"]}\nnome: {livro["nome"]}')
                        print(f'autor: {livro["autor"]}\neditora: {livro["editora"]}\n')
                if not conta_id:
                    print(f'Desculpe, não foi possível encontrar o livro com id {consulta_id}.')
            elif op2 == 3:
                # Consulta livro por autor
                consulta_autor = input('Digite o autor do(s) livro(s): ').upper()
                conta_autor = False
                print("-" * 16)
                for livro in lista_livro:
                    if livro['autor'] == consulta_autor:
                        conta_autor = True
                        print(f'id: {livro["id"]}\nnome: {livro["nome"]}')
                        print(f'autor: {livro["autor"]}\neditora: {livro["editora"]}\n')
                if not conta_autor:
                    print(f'Desculpe, não há livros do(a) {consulta_autor} registrados em nossa livraria.')
            elif op2 == 4:
                # Retorna para o menu principal
                break
            else:
                print('Opção inválida.\n')
                continue
        except ValueError:
            print('Caractere inválido.\n')
        print(f'{"-" * 16}\n{"-" * 50}\n')


def remover_livro():
    # Opção 3 escolhida
    while True:
        try:
            print("-" * 50)
            print("-" * 10, 'MENU REMOVER LIVRO', "-" * 18)
            id = int(input('Digite o id do livro a ser removido: '))
            id_livro = 0
            for livro in lista_livro:
                if livro['id'] != id:
                    id_livro += 1
                else:
                    break
            del lista_livro[id_livro]
            print('Livro removido com sucesso!')
            break
        except IndexError:
            print('Id inválido.\n')
            continue


# Programa principal
print('Bem-vindo a Livraria da Pietra Ataulo')
lista_livro = []
id_global = 0
while True:
    try:
        print("-" * 50)
        print("-" * 15, 'MENU PRINCIPAL', "-" * 19)
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
            print('Opção inválida.\n')
            continue
    except ValueError:
        print('Caractere inválido.\n')
