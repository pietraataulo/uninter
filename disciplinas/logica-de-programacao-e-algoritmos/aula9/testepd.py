import pandas as pd
import re

df = pd.read_csv("https://raw.githubusercontent.com/leonhgomes/Pandas/main/pokemon_data.csv")

# Acessando o nome das colunas e o início e fim da tabela
# print(df.columns)
# print(df.head(3)) # acessa 3 primeiros dados
# print(df.tail(3)) # acessa 3 dados finais

# Acessar colunas individuais
# print(df[['Nome', 'Tipo 1']][5:10])

# Acessar dados individuais
# print(df.iloc[:7]) # i = índice
# print(df.loc[df['Lendario']])

# Acessar linhas por nome
#for indice, linha in df.iterrows():
    #print(indice, linha['Nome'])
    #if linha['#'] == 150:
        #break

# Valores estatísticos básicos
#print(df.describe())

# Ordenar por ordem alfabética
# print(df.sort_values('Nome'))

# Realizando mudanças nos dados
# df['Total'] = df['Ataque'] + df['Atq Esp'] + df['Def Esp'] + df['Defensa'] + df['Velocidade'] + df['Vida']
# print(df['Total'])

# Removendo coluna
# df.drop(columns=['Total'])

# Renomeando
#df.rename({'Defensa': 'Defesa'},axis=1)

# Salvando arquivo
#df.to_csv('modificado.csv',index=False) # index=False não mostra a coluna padrão de índice

# & E, | OU, ~ NÃO

# Fogo ou água tipo 1
#novo_df = df.loc[df['Tipo 1'].str.contains('Fogo|Agua',flags=re.I,regex=True)]
#print(novo_df['Tipo 1'])


# Expressões regulares
# ^ Começa com. EXEMPLO: '^pi' começa com pi
# $ Termina com.

# Mudanças condicionais
#df.loc[df['Tipo 1'] == 'Fogo', 'Tipo 1'] = 'Fogueteiro'
 # Localiza pokemon de fogo ///  Retorna tipo 1

# histograma
import matplotlib.pyplot as plt
#atributo='Ataque'
#bins = range(0, 201, 20)
#plt.xticks(bins)

#plt.title('Distribuição dos pokemons por ' + atributo)
#plt.xlabel('Valor do atributo ' + atributo)
#plt.ylabel('Quantidade de pokemons')
#plt.hist(df[atributo],bins=bins)
#plt.show()

# barra vertical
atributo='Ataque'
tipos = df.groupby('Tipo 1').mean(numeric_only=True).sort_values(atributo,ascending=False)
linha = tipos.index.tolist()
coluna = tipos[atributo].tolist()
figura = plt.figure(figsize=(14,4)).add_axes([0,0,1,1])
figura.bar(linha,coluna)

plt.xlabel('Tipos de pokemons')
plt.ylabel('Valor médio do atributo ' + atributo)
plt.title('Valor médio do atributo' + atributo + 'por tipo de pokemon')


plt.show()