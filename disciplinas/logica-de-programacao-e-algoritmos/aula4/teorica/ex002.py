# Valor inicial e final
inicial = int(input('Digite o valor inicial:'))
final = int(input('Digite o valor final:'))
cont = inicial
pos = 0
par = 0
imp = 0
soma_par = 0
soma_imp = 0
soma_pos = 0

# Repetição
while (cont <= final):
    print(inicial)
    if inicial > 0:
        pos += 1
        soma_pos += inicial
    if inicial % 2 == 0:
        par += 1
        soma_par += inicial
    else:
        imp += 1
        soma_imp += inicial
    inicial += 1
    cont += 1
    
print(f'Números positivos: {pos}\nPares: {par}\nÍmpares: {imp}\nMédia dos valores positivos: {soma_pos/cont}\nMédia dos pares: {soma_par/cont}\nMédia dos ímpares: {soma_imp/cont}')