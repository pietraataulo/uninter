# Funções
def escolha_servico():
    # Menu e custo por página
    while True:
        print('\nEntre com o tipo de serviço desejado')
        print('DIG - Digitalização\nICO - Impressão Colorida')
        print('IPB - Impressão Preto e Branco\nFOT - Fotocópia')
        serv = input('>>')
        if serv == 'dig':    # Serviço de digitalização escolhido
            return 1.10
        elif serv == 'ico':  # Serviço de impressão colorida escolhido
            return 1
        elif serv == 'ipb':  # Serviço de impressão preto e branco escolhido
            return 0.40
        elif serv == 'fot':  # Serviço de fotocópia escolhido
            return 0.20
        else:  # Errou o serviço
            print('Escolha inválida, entre com o tipo do serviço novamente ')
            continue


def num_pagina():
    # Desconto por número de páginas
    while True:
        try:
            paginas = int(input('Entre com o número de páginas: '))
            if paginas >= 20000:
                print('Não aceitamos tantas páginas de uma vez.')
                print('Por favor, entre com  número de páginas novamente.\n')
                continue
        except ValueError:
            print('Caractere inválido. Tente novamente...\n')
        else:
            break
    # Desconto por número de páginas tratadas
    if paginas >= 2000:  # Número de páginas maior ou igual a 2000 (e menor que 20000)
        valor = paginas * 0.75
    elif 200 <= paginas < 2000:  # Número de páginas maior ou igual a 200 e menor que 2000
        valor = paginas * 0.80
    elif 20 <= paginas < 200:  # Número de páginas maior ou igual a 20 e menor que 200
        valor = paginas * 0.85
    else:  # Número de páginas menor que 20
        valor = paginas
    return valor


def servico_extra():
    # Serviço extra
    while True:
        print('\nDeseja adicionar algum serviço?')
        print('1 - Encadernação Simples - R$ 15.00')
        print('2 - Encadernação Capa Dura - R$ 40.00')
        print('0 - Não desejo mais nada')
        extra = int(input('>>'))
        if extra == 1:  # Encadernação simples
            return 15
        elif extra == 2:  # Capa dura
            return 40
        elif extra == 0:  # Sem adicional
            return 0
        else:
            continue


# Programa principal
print('Bem vindo a Copiadora da Pietra Ataulo')
custo_pag = escolha_servico()  # Valor do serviço
desc_pag = int(num_pagina())  # Valor da página
valor_extra = servico_extra()  # Valor adicional
total = custo_pag * desc_pag + valor_extra
print(f'Total: R$ {total:.2f} (serviço: {custo_pag:.2f} * páginas: {desc_pag} + extra: {valor_extra:.2f})')
