
def varredura(lista, dado):
    x = 0
    while x < len(lista):
        if lista[x] == dado:
            return x
        x += 1
    return -1

lista = ['macarrão', 'tomate', 'batata', 'queijo']
dado = 'macarrão'
x = varredura(lista, dado)
print(x)

