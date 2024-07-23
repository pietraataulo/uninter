print(f'Bem-vindo a Loja de Gelados da Pietra Ataulo\n{'-' * 20}' + 'Cardápio' + f'{'-' * 20}\n{'-' * 48}')
# Imprimindo o cardápio
print(f'{'-' * 3}| Tamanho  |  Cupuaçu (CP)  |  Açaí (AC) |{'-' * 3}\n{'-' * 3}|    P     |    R$  9.00    |  R$ 11.00  |{'-' * 3}\n{'-' * 3}|    M     |    R$  14.00   |  R$ 16.00  |{'-' * 3}\n{'-' * 3}|    G     |    R$  18.00   |  R$ 20.00  |{'-' * 3}\n{'-' * 48}')

# Montando o pedido
valor = 0
while True:
    sabor = input('Entre com o sabor desejado (CP/AC): ')
    if sabor == 'cp' or sabor == 'CP':
        # Sabor cupuaçu
        tamanho = input('Entre com o tamanho desejado (P/M/G): ')
        if tamanho == 'p' or tamanho == 'P':
            # Tamanho P
            valor += 9
            print(f'Você pediu um Cupuaçu no tamanho P: R$ 9.00')
            extra = input('\nDeseja mais alguma coisa? (S/N):')
            if extra == 's' or extra == 'S':
                continue
            else:
                break
        elif tamanho == 'm' or tamanho == 'M':
            # Tamanho M
            valor += 14
            print(f'Você pediu um Cupuaçu no tamanho M: R$ 14.00')
            extra = input('\nDeseja mais alguma coisa? (S/N): ')
            if extra == 's' or extra == 'S':
                continue
            else:
                break
        elif tamanho == 'g' or tamanho == 'G':
            # Tamanho G
            valor += 18
            print(f'Você pediu um Cupuaçu no tamanho G: R$ 18.00')
            extra = input('\nDeseja mais alguma coisa? (S/N): ')
            if extra == 's' or extra == 'S':
                continue
            else:
                break
        else:
            print('Tamanho inválido. Tente novamente')
            continue
    elif sabor == 'ac' or sabor == 'AC':
        # Sabor açaí
        tamanho = input('Entre com o tamanho desejado (P/M/G): ')
        if tamanho == 'p' or tamanho == 'P':
            # Tamanho P
            valor += 11
            print(f'Você pediu um Açaí no tamanho P: R$ 11.00')
            extra = input('\nDeseja mais alguma coisa? (S/N):')
            if extra == 's' or extra == 'S':
                continue
            else:
                break
        elif tamanho == 'm' or tamanho == 'M':
            # Tamanho M
            valor += 16
            print(f'Você pediu um Açaí no tamanho M: R$ 16.00')
            extra = input('\nDeseja mais alguma coisa? (S/N): ')
            if extra == 's' or extra == 'S':
                continue
            else:
                break
        elif tamanho == 'g' or tamanho == 'G':
            # Tamanho G
            valor += 20
            print(f'Você pediu um Açaí no tamanho G: R$ 20.00')
            extra = input('\nDeseja mais alguma coisa? (S/N): ')
            if extra == 's' or extra == 'S':
                continue
            else:
                break
        else:
            print('Tamanho inválido. Tente novamente')
            continue
    else:
        print('Sabor inválido. Tente novamente')
        continue
# Total a ser pago
print(f'\nO valor total a ser pago: R$ {valor:.2f}')

