# Lendo números inteiros
soma = 0
qtd_num = 0
x = 0
while True:
    x = int(input('Digite um valor inteiro:'))
    if x < 0:
        print('Apenas positivos')
        continue
    
    if not x:
        break
    soma += x
    qtd_num += 1
    
print(f'A média dos valores é: {soma/qtd_num}')
      