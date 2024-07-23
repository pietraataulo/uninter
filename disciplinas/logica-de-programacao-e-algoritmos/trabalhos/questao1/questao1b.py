# Apresentando a loja e solicitando informações
print('Bem-vindo a Loja da Pietra Ataulo')
valor_produto = float(input('Entre com o valor do produto: '))
qtd_produto = int(input('Entre com a quantidade do produto: '))
valor_compra = valor_produto * qtd_produto

if valor_compra >= 10000:
    # Caso o valor da compra seja maior que 10000
    valor_final = valor_compra * 0.89
    print(f'O valor SEM desconto: R${valor_compra:.2f}\nO valor COM desconto: R${valor_final:.2f}')
elif valor_compra >= 6000 and valor_compra < 10000:
    # Caso o valor da compra seja maior que 6000 e menor que 10000
    valor_final = valor_compra * 0.93
    print(f'O valor SEM desconto: R${valor_compra:.2f}\nO valor COM desconto: R${valor_final:.2f}')
elif valor_compra >= 2500 and valor_compra < 6000:
    # Caso o valor da compra seja maior que 2500 e menor que 6000
    valor_final = valor_compra * 0.96
    print(f'O valor SEM desconto: R${valor_compra:.2f}\nO valor COM desconto: R${valor_final:.2f}')
elif valor_compra > 0 and valor_compra < 2500:
    # Caso o valor da compra seja maior que 0 e menor que 2500
    valor_final = valor_compra 
    print(f'O valor SEM desconto: R${valor_compra:.2f}\nO valor COM desconto: R${valor_final:.2f}')
else:
    # Caso o cliente digite um valor negativo
    print('Valor inválido.')

