
print('Bem vindo a Copiadora da Pietra Ataulo')

# Menu e custo por página
def escolha_servico():
    while True:
        print('\nEntre com o tipo de serviço desejado')
        print('DIG - Digitalição\nICO - Impressão Colorida')
        print('IPB - Impressão Preto e Branco\nFOT - Fotocópia')
        serv = input('>>')
        if serv == 'dig':
            custo_pag = 1.10
            break
        elif serv == 'ico':
            custo_pag = 1
            break
        elif serv == 'ipb':
            custo_pag = 0.40
            break
        elif serv == 'fot':
            custo_pag = 0.20
            break
        else:
            print('Escolha inválida, entre com o tipo do serviço novamente ')
            continue
    return custo_pag

custo_pag = escolha_servico() # Valor da página

# Desconto por número de páginas
def num_pagina():
    while True:
        try:
            paginas = int(input('Entre com o número de páginas: '))
            if paginas >= 20000:
                print('Não aceitamos tantas páginas de uma vez.')
                print('Por favor, entre com  número de páginas novamente.\n')
                continue
            else:
                break
        except ValueError:
            print('Caractere inválido. Tente novamente...\n') 
    # Desconto por número de páginas tratadas
    if paginas >= 2000:
        desconto = 0.75
    elif 200 >= paginas < 2000:
        desconto = 0.80
    elif 20 >= paginas < 200:
        desconto = 0.85
    else:
        desconto = 1
    valor = paginas * desconto
    return valor


n = int(num_pagina())

# Serviço extra
def servico_extra():
    while True:
        print('Deseja adicionar algum serviço?')
        print('1 - Encadernação Simples - R$ 15.00')
        print('2 - Encadernação Capa Dura - R$ 40.00')
        print('0 - Não desejo mais nada')
        extra = int(input('>>'))
        if extra == 1: # Encadernação simples
            valor_adicional = 15
            break
        elif extra == 2: # Capa dura
            valor_adicional = 40
            break
        elif extra == 0: # Sem adicional
            valor_adicional = 0
            break
        else:
            continue
    return valor_adicional

valor_extra = servico_extra()
print(valor_extra)

# Calculando o total