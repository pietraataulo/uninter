# Ler dois valores
num1 = float(input('Digite o primeiro valor:'))
num2 = float(input('Digite o segundo valor:'))
count = 1
soma = 0

# Calculando com while
# 2 x 5 = 5 + 5
# 3 x 5 = 5 + 5 + 5

while (count <= num1):
    soma += num2
    count += 1
print(f'{num1} x {num2} = {soma}')