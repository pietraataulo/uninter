def valida_int(pergunta, min, max):
    x = int(input(pergunta))
    while x < min or x > max:
        x = int(input(pergunta))
    return x

# Programa principal
res = valida_int('Digite um valor inteiro: ', 0, 100) # resultado da função vai retornar para cá pois foi o Res quem chamou a função
print(f'Você digitou {res}. Encerrando o programa...')