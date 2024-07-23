print('Digite uma mensagem que irei repetir pra você')
print('Para encerrar, escreva "sair"')
texto = input('')
while True:
    texto = input('')
    print(texto)
    if texto == 'sair':
        break