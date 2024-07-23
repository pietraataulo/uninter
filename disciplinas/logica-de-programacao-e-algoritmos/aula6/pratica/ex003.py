# Jokenpô
import random


def valida_int(pergunta, min, max):
    x = int(input(pergunta))
    while x < min or x > max:
        x = int(input(pergunta))
    return x

def vencedor(jogador1, jogador2):
    global v1, v2, empate
    if jogador1 == 1: # pedra
        if jogador2 == 1: # pedra
            empate += 1
        elif jogador2 == 2: # papel
            v2 += 1
        else: # Tesoura
            v1 += 1
    elif jogador1 == 2: # papel
        if jogador2 == 1: # pedra
            v1 += 1
        elif jogador2 == 2: # papel
            empate += 1
        else: # Tesoura
            v2 += 1
    elif jogador1 == 3: # tesoura
        if jogador2 == 1: # pedra
            v2 += 1
        elif jogador2 == 2: # papel
            v1 += 1
        else: # Tesoura
            empate += 1
    
    resultados = [v1, v2, empate]
    return resultados

print('JOKENPÔ')
print('1 - Pedra')
print('2 - Papel')
print('3 - Tesoura')

jogadas = []
resultados = []
v1 = 0
v2 = 0
empate = 0

while True:
    j1 = valida_int('Escolha sua jogada: ', 0, 3)
    if not j1:
        break
    j2 = random.randint(1,3)
    jogadas.append([j1, j2])
    resultados = vencedor(j1, j2)

for jogada in jogadas:
    for dado in jogada:
        print(dado, end=' ')
    print()

print(f'Número de vitórias do jogador 1: {resultados[0]}')
print(f'Número de vitórias do jogador 2: {resultados[1]}')
print(f'Número de empates: {resultados[2]}')
