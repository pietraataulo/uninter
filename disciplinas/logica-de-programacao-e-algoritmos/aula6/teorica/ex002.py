def func_maior(mensagem, *num):
    maior = 0
    for item in num:
        if item > maior:
            maior = item
    print(mensagem, maior)

func_maior('Números são complexos', 2, 3, 8, 40, 1, 9)
