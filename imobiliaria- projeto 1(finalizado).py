#Aula 01
 #1- carregue o conjunto de dados kc_house_data.csv do hd para memoria
import pandas   as pd
data = pd.read_csv('datasets/kc_house_data.csv')

#2 - Mostre as cincos primeiras linhas do meu conjunto de dados
print(data.head() )

# 3- Mostre o numero de linhas do conjunto de dados
print(data.shape)

#4- mostre na tela o nome das colunas do conjunto de dados
print(data.columns)


#5-  mostre na tela o conjunto de dados ordenados pela coluna price
#6- mostre na tela o conjunto de dados ordenados pela coluna price ordenando pelo maior preço
print(data[['id', 'price']].sort_values('price' , ascending = False))

# 1. Quantas casas estao disponiveis para alugar?
print(data.shape)
#R: No total 21613 casas estao disponiveis para alugar.

# 2. Quantos atributos as casas possuem?
print(data.shape)
#R: Essas casas possuem ao todo 21 atributos

#3. Quais sao os atributos das casa?
print(data.columns)
#R: ['id', 'date', 'price', 'bedrooms', 'bathrooms', 'sqft_living',
       'sqft_lot', 'floors', 'waterfront', 'view', 'condition', 'grade',
       'sqft_above', 'sqft_basement', 'yr_built', 'yr_renovated', 'zipcode',
       'lat', 'long', 'sqft_living15', 'sqft_lot15']

#4. Qual a casa mais cara?
print(data[["price","id"]].sort_values('price', ascending= False))
#R: A casa mais cara é a casa 7252 com valor de $7.700.000,00

#5.Qual a casa com mais numero de quartos?
print(data[["bedrooms","id"]].sort_values('bedrooms', ascending= False))
#R: A casa com o maior numero de quartos é a casa 15870 contendo 33 quartos.

# 6. Qual a soma total de quartos do conjunto de dados?
print(data[['bedrooms']].sum () )
#R: A soma total de quartos do conjunto de dados é 72854

# 7.Quantas casas possuem 2 banheiros?
print ( data[['id','bedrooms']].query("bedrooms ==2"))
#R: Das 21613 casas disponíveis, 2760 possuem 2 banheiros

# 8 Qual o preco medio de todas as casas?
aver_price = data[['price']]
print(aver_price.mean())
#R: O preco medio das casas e de $540.008,14

#9. Qual o preço minimo entre as casa com 2 banheiros ?
data = pd.read_csv('datasets/kc_house_data.csv')
data2= ( data[['id','bedrooms','price']].query("bedrooms ==2"))
print(data2[['id', 'price','bedrooms']].sort_values('price' , ascending = True))
#R: O preço minimo entre as casas com 2 banheiro e de $78.000,00

#10. Qual o preco medio entre as casas com 3 quartos?
data2= ( data[['bedrooms','price']].query("bedrooms ==3"))
print(data2.mean())
#R: O preco medio entre as casas de 3 quarto e $466.232,07

#11. Quantas casas possuem mais de 300 metros quadrados ?
 300m² = 3229,17 sqft
print(data[['sqft_lot','id']].query('sqft_lot >= 3229.17'))
R:19.519 possuem mais de 300m².

#12.Quantas casas tem mais de 2 andares ?
print(data[['floors','id']].query('floors > 2'))
#R: Ao todo no banco de dados tem 782


#13.Quantas casas tem vista para o mar? 163
print(data[['waterfront','id']].query('waterfront >=1'))
#R: 163 casas possuem vista para o mar


#14. Das casas com vista para o mar, quantas tem 3 quartos ?
data_wf = (data.query('waterfront >=1'))
print(data_wf.query('bedrooms == 3'))
R: 64 casas possuem 3 quartos e vista para o mar.
