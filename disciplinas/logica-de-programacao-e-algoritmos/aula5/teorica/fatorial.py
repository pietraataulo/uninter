def fatorial(num):
    fat = 1
    while num > 1:
        fat *= num
        num -= 1
    return fat

# programa principal
x = fatorial(int(input('Digite um número: ')))
print(x)