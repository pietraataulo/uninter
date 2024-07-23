def buscaSequencial(lista, dado):

  x = 0

  while x < len(lista):

    if (lista[x] == dado):

      return x

    x += 1

  return -1

#Programa principal

teste = [3,7,9,1,0,7,5,12]

#utilize o tipo de dado que quiser, basta alterar aqui

dado = int(input('Digite um valor inteiro: '))

res = buscaSequencial(teste, dado)

if res >= 0:

  print(f'Posição onde o {dado} foi encontrado: {res + 1}')

else:

  print('Dado não localizado...')