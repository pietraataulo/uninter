# Apresentando a loja e solicitando informações
print('Bem-vindo a Loja da Pietra Ataulo')
valor_produto = float(input('Entre com o valor do produto: '))
qtd_produto = int(input('Entre com a quantidade do produto: '))
valor_compra = valor_produto * qtd_produto

# Verificando o desconto
if valor_compra >= 10000:
    # Valor maior ou igual a 10000
    valor_final = valor_compra * 0.89
elif 6000 <= valor_compra < 10000:
    # Valor maior ou igual a 6000 e menor que 10000
    valor_final = valor_compra * 0.93
elif 2500 <= valor_compra < 6000:
    # Valor maior ou igual a 2500 e menor que 6000
    valor_final = valor_compra * 0.96
else:
    # Nenhum dos valores acima/Menor que 2500
    valor_final = valor_compra
# Imprimindo os valores com e sem desconto
print(f'O valor SEM desconto: R${valor_compra:.2f}\nO valor COM desconto: R${valor_final:.2f}')
