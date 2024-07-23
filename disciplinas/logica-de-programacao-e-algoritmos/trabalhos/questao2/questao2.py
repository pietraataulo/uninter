print(f'Bem-vindo a Loja de Gelados da Pietra Ataulo\n{"-" * 20}' + 'Cardápio' + f'{"-" * 20}\n{"-" * 48}')
# Imprimindo o cardápio
print(f'{"-" * 3}| Tamanho  |  Cupuaçu (CP)  |  Açaí (AC) |{"-" * 3}')
print(f'{"-" * 3}|    P     |    R$  9.00    |  R$ 11.00  |{"-" * 3}')
print(f'{"-" * 3}|    M     |    R$  14.00   |  R$ 16.00  |{"-" * 3}')
print(f'{"-" * 3}|    G     |    R$  18.00   |  R$ 20.00  |{"-" * 3}\n{"-" * 48}')
# Montando o pedido
valor = 0
while True:
    sabor = input('Entre com o sabor desejado (CP/AC): ')
    if sabor == 'cp' or sabor == 'CP':
        # Sabor cupuaçu
        sabor = 'Cupuaçu'
        tamanho = input('Entre com o tamanho desejado (P/M/G): ')
        if tamanho == 'p' or tamanho == 'P':
            # Cupuaçu tamanho P
            tamanho = 'P'
            preco = 9
            valor += 9
        elif tamanho == 'm' or tamanho == 'M':
            # Cupuaçu tamanho M
            tamanho = 'M'
            preco = 14
            valor += 14
        elif tamanho == 'g' or tamanho == 'G':
            # Cupuaçu tamanho G
            tamanho = 'G'
            preco = 18
            valor += 18
        else:
            # Errou o tamanho do cupuaçu
            print('Tamanho inválido. Tente novamente.\n')
            continue
    elif sabor == 'ac' or sabor == 'AC':
        # Sabor açaí
        sabor = 'Açaí'
        tamanho = input('Entre com o tamanho desejado (P/M/G): ')
        if tamanho == 'p' or tamanho == 'P':
            # Açaí tamanho P
            tamanho = 'P'
            preco = 11
            valor += 11
        elif tamanho == 'm' or tamanho == 'M':
            # Açaí tamanho M
            tamanho = 'M'
            preco = 16
            valor += 16
        elif tamanho == 'g' or tamanho == 'G':
            # Açaí tamanho G
            tamanho = 'G'
            preco = 20
            valor += 20
        else:
            # Errou o tamanho do açaí
            print('Tamanho inválido. Tente novamente.\n')
            continue
    else:
        # Errou o sabor
        print('Sabor inválido. Tente novamente.\n')
        continue
    print(f'Você pediu um {sabor} no tamanho {tamanho}: R$ {preco:.2f}')
    extra = input('\nDeseja mais alguma coisa? (S/N): ')
    if extra == 's' or extra == 'S':
        continue
    else:
        break
# Total a ser pago
print(f'\nO valor total a ser pago: R$ {valor:.2f}')
