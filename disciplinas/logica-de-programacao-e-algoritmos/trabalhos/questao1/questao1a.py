# Apresentando a loja e solicitando informações
print('Bem-vindo a Loja da Pietra Ataulo')
valor_produto = float(input('Entre com o valor do produto: '))
qtd_produto = int(input('Entre com a quantidade do produto: '))

# Verificando o desconto 
valor_compra = valor_produto * qtd_produto

if valor_compra >= 10000:
    valor_final = valor_compra * 0.89
elif valor_compra >= 6000 and valor_compra < 10000:
    valor_final = valor_compra * 0.93
elif valor_compra >= 2500 and valor_compra < 6000:
    valor_final = valor_compra * 0.96
else:
    valor_final = valor_compra

# Imprimindo os valores com e sem desconto
print(f'O valor SEM desconto: R${valor_compra:.2f}\nO valor COM desconto: R${valor_final:.2f}')
    

