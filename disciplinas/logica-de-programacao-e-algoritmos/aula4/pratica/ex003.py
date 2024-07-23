total = 0
dinheiro = 0
i = 0

while True:
    idade = int(input('Qual sua idade? '))
    if idade == 0:
        break

    total += 1

    if idade < 3:
        ingresso = 0
    else:
        if idade > 12:
            ingresso = 30
        else:
            ingresso = 15
    dinheiro += ingresso
    i += idade
if total > 0:
    media = i / total
    print(f'Total de pessoas: {total}')
    print(f'Total arrecadado: {dinheiro}')
    print(f'Média de idades: {media}')