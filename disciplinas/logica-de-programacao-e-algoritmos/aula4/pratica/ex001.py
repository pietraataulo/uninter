print('LANCHONETE')
print('1 - Coxinha R$ 5,00\n2 - Pastel R$ 7,00')
print('3 - Coxinha R$ 4,00\n4 - Suco R$ 6,00')
print('5 - SAIR')

total = 0
while True:
    op = int(input('Qual item gostaria de comprar? '))
    

    if (op == 1):
         qtd = int(input('Quantas unidades quer comprar? '))
         total = total + qtd * 5
    elif (op == 2):
         qtd = int(input('Quantas unidades quer comprar? '))
         total = total + qtd * 7
    elif (op == 3):
         qtd = int(input('Quantas unidades quer comprar? '))
         total = total + qtd * 4
    elif (op == 4):
         qtd = int(input('Quantas unidades quer comprar? '))
         total = total + qtd * 6
    elif (op == 5):
        break
    else:
        print('Produto inválido. Selecione outro.')

print(f'O total a ser gasto neste pedido é de R$ {total:.2f}')