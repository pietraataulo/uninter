notas = list()
x = float(input('Digite uma nota:'))
while x >= 0:
    notas.append(x)
    x = float(input('Digite uma nota:'))
soma = 0
for valores in notas:
    soma += valores
media = soma/len(notas)
print(notas)
print(media)