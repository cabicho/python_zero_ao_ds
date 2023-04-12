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
print(data[['id', 'price']].sort_values('price', ascending=False))
