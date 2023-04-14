import pandas as pd
#pip install pandas
print('hello world')

import os

diretorio = os.path.dirname(os.path.realpath(("kc_house_data.csv")))
print(diretorio)

data=pd.read_csv('/home/joneldigitalmz/curso_python_zero_ao_ds/datasets/kc_house_data.csv')
# mostrar na tela as 5 primeiras linhas do conjunto de dados
print(data.head())

# mostre o numero de colunas e de linhas do conjunto de dados
print(data.shape[0])

# mostre na tela o nome das colunas do conjunto de dados
atributos=data.columns
print('Os atributos do conjunto de dados sao: ' + str(atributos.values))

#moste na tela o conjudo de dados ordenados pela coluna price
#print(data[['id', 'price']].sort_values('price', ascending=False))

#Resolvendo os exercicios adicionais
#6. Qual a soma total de quartos do conjunto de dados?
#R:  print('A soma total de quartos do conjunto de dados é ',data[['bedrooms']].sum())
#print('Os atributos do conjunto de dados sao: ' + str(atributos.values))

# 7. Quantas casas possuem 2 banheiros?
print( data.loc[data['bedrooms']>2].shape[0], 'casas possuem 2 banheiros',)
#https://www.delftstack.com/howto/python-pandas/how-to-get-the-sum-of-pandas-column/

# 8. Qual o preco medio de todas as casas do conjunto?
media=data['price'].mean()
print('O valor medio de todas as casas é',  round(media,2))

# https://acervolima.com/use-pandas-para-calcular-estatisticas-em-python/
# arredondando para 2 casas
# http://www.bosontreinamentos.com.br/programacao-em-python/como-arredondar-numeros-em-python/

# 9. Qual o preco medio de casas com 2 banheiros?
media_2=data['price'].loc[data['bathrooms']==2].mean()
print('O preco medio de casas com 2 banheiros é ',round(media_2,2),)

# 10. Qual minimo preco minimo entre as casas com 3 quartos?
min=data['price'].loc[data['bedrooms']==3].min()
print('O minimo preco entre as casas com 3 quartos é ', min,)
