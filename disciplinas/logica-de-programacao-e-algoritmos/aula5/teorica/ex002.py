def destaque(palavra):
    tam = len(palavra)
    print('+', '-' * tam, '+')
    print('|', palavra, '|')
    print('+', '-' * tam, '+')

destaque(input('Digite uma palavra: '))
