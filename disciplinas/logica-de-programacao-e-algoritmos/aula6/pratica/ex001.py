notas = [9, 7, 7, 10, 3, 9, 6, 6, 2]
notas[-1] = 4
nota7 = 0
notas.sort() # Ordenar

print(sum(notas) // len(notas)) # Média
print(max(notas)) # Maior valor 
print(notas.count(7)) # Contagem
print(notas)
