aluno = {}

aluno['nome'] = input('Qual o nome do aluno?')

n1 = float(input('Qual a primeira nota?'))

n2 = float(input('Qual a segunda nota?'))

n3 = float(input('Qual a terceira nota?'))

aluno['media'] = (n1 + n2 + n3) / 3

if aluno['media'] >= 7:

  aluno['status'] = 'A'

elif aluno['media'] >= 5 and aluno['media'] < 7:

  aluno['status'] = 'E'

else:

  aluno['status'] = 'R'

for chave, valor in aluno.items():

  print(f'{chave} = {valor}')
