lista = []
while True:
    nome = input('Digite seu nome: ')
    if nome == 'sair':
        break
    altura = float(input('Digite sua altura: '))
    peso = float(input('Digite seu peso: '))
    imc = peso//(altura * altura)
    lista.append([nome, altura, peso, imc])

maior = 0
menor = 99
for cadastro in lista:
    if cadastro[2] > maior:
        maior = cadastro[2]
    if cadastro[2] < menor:
        menor = cadastro[2]

print(lista)
print(len(lista))
print(maior)
print(menor)