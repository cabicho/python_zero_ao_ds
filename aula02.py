import pandas as pd

#data=pd.read_csv('/home/joneldigitalmz/curso_python_zero_ao_ds/datasets/kc_house_data.csv')
data=pd.read_csv('datasets/kc_house_data.csv')
# mostrar na tela as 5 primeiras linhas do conjunto de dados
print(data.dtypes)

#1. Qual a data do imovel, mais antigo
data['date']=pd.to_datetime(data['date'])
data_=data[['date']].sort_values('date', ascending=True)
#print(data.iloc([0, axis=1]))
data_min=data_.min()
print('minimo', data_min)
data_max=data_.max()
print('maxima data', data_max)

#2. Quantos imoveis possuem o numero maximo de andares?
#data['floors']=pd.to_int(data['floors'])
#data['floors']=data['floors'].astype('int')
#print(data['floors'].unique())
max_andar=data[['floors']].max()
print(max_andar)
max_andar=data[['floors']].min()
print('min', max_andar)
print(data[data['floors']==3.5][['id','floors']].shape[0], 'imoveis possuem o numero maximo de andares')

#3. Criar uma classificacao para o imoveis, separando-os em baixo e alto, de acordo com o preco
data['padrao']='data[padrao]'
data.loc[data['price']>540000, 'padrao']='alto'
data.loc[data['price']<540000, 'padrao']='baixo'
print(data['padrao'])

#4. Gostaria de um relatorio, ordenado pelo preco
#4)	Relatorio ordenado pelo preco e contendo as seguinte informações: 
# (id, data da disponibilidade, numero de quartos, tamanho total do terreno, peço e a classificação do imóvel(alto, baixo padrão)

import os

diretorio = os.path.dirname(os.path.realpath(("kc_house_data.csv")))

print(diretorio)
print(diretorio+'/datasets/')

campos = ['id','date', 'floors', 'sqft_lot','price','padrao']
print(data[campos].sort_values('price', ascending=False))
report=data[campos].sort_values('price', ascending=False)

report.to_csv(diretorio+'/datasets/report_aula02.csv', index=False)


#1:46:46
#5)	Gostaria de num mapa ver indicando onde as casas estão localizadas geograficamente
#a.	Procurar uma biblioteca em python que armazena uma função que desenha mapa
#b.	Aprender a usar a função que desenha mapas
# Plotly - Biblioteca que armazena uma funcao que desenha mapa
# scatter MapBox - funcao que desenha mapa

# pip install plotly
import plotly.express as px 

data_mapa=data[['id', 'lat', 'long','price']]
mapa = px.scatter_mapbox(data_mapa, lat='lat', lon='long', hover_name='id',hover_data=['price'], color_discrete_sequence=['fuchsia'], zoom=3, height=300)

mapa.update_layout(mapbox_style='open-street-map')
mapa.update_layout(height=600, margin={'r':0, 't':0, 'l':0, 'b':0})
mapa.show()

mapa.write_html(diretorio+'/datasets/mapa_house_rocket.html')
# #data['bedrooms']=data['bedrooms'].astype(float64)
# delectar variveis
# data['eusou']='mais que vencedor em Cristo Jesus'
# print(data.dtypes)
# # data = data.drop('', axis=1)
# print(data['eusou'])
# data=data.drop('eusou', axis=1)
# print(data.dtypes)

# dados[linhas, colunas]
#print(data.iloc[0:10, 0:3])

# forma 04: indice Booleanos [0,1], [False, True]



# 1)	Qual a data do imovel mais antiga no portfolio?
# a.	Idenficiar qual a data mais antiga e de seguida procurar o imóvel a data encontrada


#print(min(data['date'], axis=0))

# print(data.dtypes[:4])
# e' necessario prestar atencao nos tipos das variaveis

# mostre o numero de colunas e de linhas do conjunto de dados
# print(data.shape[0])

# mostre na tela o nome das colunas do conjunto de dados
#atributos=data.columns
#print('Os atributos do conjunto de dados sao: ' + str(atributos.values))

#moste na tela o conjudo de dados ordenados pela coluna price
#print(data[['id', 'price']].sort_values('price', ascending=False))

#Resolvendo os exercicios adicionais
#6. Qual a soma total de quartos do conjunto de dados?
#R:  print('A soma total de quartos do conjunto de dados é ',data[['bedrooms']].sum())
#print('Os atributos do conjunto de dados sao: ' + str(atributos.values))

# 7. Quantas casas possuem 2 banheiros?
#print( data.loc[data['bedrooms']>2].shape[0], 'casas possuem 2 banheiros',)
#https://www.delftstack.com/howto/python-pandas/how-to-get-the-sum-of-pandas-column/

# 8. Qual o preco medio de todas as casas do conjunto?
#media=data['price'].mean()
#print('O valor medio de todas as casas é',  round(media,2))

# https://acervolima.com/use-pandas-para-calcular-estatisticas-em-python/
# arredondando para 2 casas
# http://www.bosontreinamentos.com.br/programacao-em-python/como-arredondar-numeros-em-python/

# 9. Qual o preco medio de casas com 2 banheiros?
#media_2=data['price'].loc[data['bathrooms']==2].mean()
#print('O preco medio de casas com 2 banheiros é ',round(media_2,2),)

# 10. Qual minimo preco minimo entre as casas com 3 quartos?
#min=data['price'].loc[data['bedrooms']==3].min()
#print('O minimo preco entre as casas com 3 quartos é ', min,)


# 11. Quantas casas, possuem mais de 300 metros quadrados
#casa_mais_300=data['sqft_living'].loc[data['sqft_living']>300].count()
#print(casa_mais_300,'casas com mais de 300 metros quadrados ')

# 12. Quantas casas, tem mais de 2 andares?
#casa_mais_2_andares=data['floors'].loc[data['floors']>2].count()
#print(casa_mais_2_andares,'casas com mais de 2 andares.')

# 13. Quantas casas, tem vista ao mar?
#casa_mais_2_andares=data['waterfront'].loc[data['waterfront']==1].count()
#print(casa_mais_2_andares,'casas com vista ao mar.')

# 14. Das casas com vista para o mar, quantas tem mais de 3 quartos na sala de estar
#vista_ao_mar_e_mais_3_andares=data['waterfront'].loc[(data['waterfront']==1) & (data['bedrooms']>3)].count()
#print(vista_ao_mar_e_mais_3_andares,'casas com vista ao mar e mais de 3 quartos.')

# 15. Das casas com mais de 300 metros quadrados de sala