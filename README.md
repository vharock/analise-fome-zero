# Análise-fome-zero 

# Problema de negócio

Você acaba de ser contratado como Cientista de Dados da empresa Fome Zero, e a sua principal tarefa nesse momento é ajudar o CEO Kleiton Guerra
a identificar pontos chaves da empresa, respondendo às perguntas que ele fizer utilizando dados!
A empresa Fome Zero é uma marketplace de restaurantes. Ou seja, seu core business é facilitar o encontro e negociações de clientes e restaurantes. Os
restaurantes fazem o cadastro dentro da plataforma da Fome Zero, que disponibiliza informações como endereço, tipo de culinária servida, se possui reservas, se faz entregas e também uma nota de avaliação dos serviços e produtos do restaurante, dentre outras informações.
O CEO Guerra também foi recém contratado e precisa entender melhor o negócio para conseguir tomar as melhores decisões estratégicas e alavancar ainda mais a Fome Zero, e para isso, ele precisa que seja feita uma análise nos dados da empresa e que sejam gerados dashboards, a partir dessas análises.
O CEO também pediu que fosse gerado um dashboard que permitisse que ele visualizasse as principais informações das perguntas que ele fez. O CEO precisa dessas informações o mais rápido possível, uma vez que ele também é novo na empresa e irá utilizá-las para entender melhor a empresa Fome Zero para conseguir tomar decisões mais assertivas.


Algumas perguntas precisam ser respondidas:

Geral:
1. Quantos restaurantes únicos estão registrados?
2. Quantos países únicos estão registrados?
3. Quantas cidades únicas estão registradas?
4. Qual o total de avaliações feitas?
5. Qual o total de tipos de culinária registrados?
   
País:
1. Qual o nome do país que possui mais cidades registradas?
2. Qual o nome do país que possui mais restaurantes registrados?
3. Qual o nome do país que possui mais restaurantes com o nível de preço igual a 4
registrados?
4. Qual o nome do país que possui a maior quantidade de tipos de culinária
distintos?
5. Qual o nome do país que possui a maior quantidade de avaliações feitas?
6. Qual o nome do país que possui a maior quantidade de restaurantes que fazem
entrega?
7. Qual o nome do país que possui a maior quantidade de restaurantes que aceitam
reservas?
8. Qual o nome do país que possui, na média, a maior quantidade de avaliações
registrada?
9. Qual o nome do país que possui, na média, a maior nota média registrada?
10. Qual o nome do país que possui, na média, a menor nota média registrada?
11. Qual a média de preço de um prato para dois por país?
   
Cidade:
1. Qual o nome da cidade que possui mais restaurantes registrados?
2. Qual o nome da cidade que possui mais restaurantes com nota média acima de
4?
3. Qual o nome da cidade que possui mais restaurantes com nota média abaixo de
2.5?
4. Qual o nome da cidade que possui o maior valor médio de um prato para dois?
5. Qual o nome da cidade que possui a maior quantidade de tipos de culinária
distintas?
6. Qual o nome da cidade que possui a maior quantidade de restaurantes que fazem
reservas?
7. Qual o nome da cidade que possui a maior quantidade de restaurantes que fazem
entregas?
8. Qual o nome da cidade que possui a maior quantidade de restaurantes que
aceitam pedidos online?

Restaurantes:
1. Qual o nome do restaurante que possui a maior quantidade de avaliações?
2. Qual o nome do restaurante com a maior nota média?
3. Qual o nome do restaurante que possui o maior valor de uma prato para duas
pessoas?
4. Qual o nome do restaurante de tipo de culinária brasileira que possui a menor
média de avaliação?
5. Qual o nome do restaurante de tipo de culinária brasileira, e que é do Brasil, que
possui a maior média de avaliação?
6. Os restaurantes que aceitam pedido online são também, na média, os
restaurantes que mais possuem avaliações registradas?
7. Os restaurantes que fazem reservas são também, na média, os restaurantes que
possuem o maior valor médio de um prato para duas pessoas?
8. Os restaurantes do tipo de culinária japonesa dos Estados Unidos da América
possuem um valor médio de prato para duas pessoas maior que as churrascarias
americanas (BBQ)?


Tipos de Culinária:
1. Dos restaurantes que possuem o tipo de culinária italiana, qual o nome do
restaurante com a maior média de avaliação?
2. Dos restaurantes que possuem o tipo de culinária italiana, qual o nome do
restaurante com a menor média de avaliação?
3. Dos restaurantes que possuem o tipo de culinária americana, qual o nome do
restaurante com a maior média de avaliação?
4. Dos restaurantes que possuem o tipo de culinária americana, qual o nome do
restaurante com a menor média de avaliação?
5. Dos restaurantes que possuem o tipo de culinária árabe, qual o nome do
restaurante com a maior média de avaliação?
6. Dos restaurantes que possuem o tipo de culinária árabe, qual o nome do
restaurante com a menor média de avaliação?
7. Dos restaurantes que possuem o tipo de culinária japonesa, qual o nome do
restaurante com a maior média de avaliação?
8. Dos restaurantes que possuem o tipo de culinária japonesa, qual o nome do
restaurante com a menor média de avaliação?
9. Dos restaurantes que possuem o tipo de culinária caseira, qual o nome do
restaurante com a maior média de avaliação?
10. Dos restaurantes que possuem o tipo de culinária caseira, qual o nome do
restaurante com a menor média de avaliação?
11. Qual o tipo de culinária que possui o maior valor médio de um prato para duas
pessoas?
12. Qual o tipo de culinária que possui a maior nota média?
13. Qual o tipo de culinária que possui mais restaurantes que aceitam pedidos
online e fazem entregas?
   

# Premissas da análise

1. Análise foi feita com dados do Dataset Zomato Restaurants - Autoupdated dataset com link para o Kaggle: https://www.kaggle.com/datasets/akashram/zomato-restaurants-autoupdated-dataset?resource=download&select=zomato.csv
2. Marketplace foi o modelo de negócio assumido.
3. As 4 principais visões de negócio foram: Visão Geral, Visão Países, Visão Cidades, Visão Tipos de Culinárias

# Estratégia da solução

O painel estratégico foi desenvolvido utilizando as métricas que
refletem as 4 principais visões do modelo de negócio da empresa:
1. Visão Geral
2. Visão Países
3. Visão Cidades
4. Visão Tipos de Culinárias Cada visão é representada pelo seguinte conjunto de métricas:
   
Cada visão é representada pelo seguinte conjunto de métricas.

1. Visão Geral
   
a. Restaurantes cadastrados
b. Países cadastrados
c. Cidades cadastradas
d. Total de avaliações feitas
e. Total de tipos de culinária registrados
f. Mapa com os restaurantes cadastrados

2. Visão Países
   
a. Quantidade de Restaurantes Registrados por país
b. Quantidade de Cidades com Restaurantes cadastrados Registradas por País
c. Média de da quantidade de Avaliações feitas por País
d. Média do Preço de um prato para duas pessoas por País

3. Visão Cidades
   
a. Top 10 Cidades com mais Restaurantes na Base de Dados
b. Top 7 Cidades com Restaurantes com média de avaliação acima de 4
c. Top 7 Cidades com Restaurantes com média de avaliação abaixo de 2.5
d. Top 10 Cidades mais restaurantes com tipos culinários distintos

3. Visão Tipod de Culinária
   
a. Melhores Restaurantes com tipos de Culinárias: Italiana, Americana, Árabe, Japonesa e Brasileira
b. Top Restaurantes ordenados por média de nota
c. Top melhores tipos de culinárias
d. Top piores tipos de culinárias


# Top Insights da análise

1. Domínio da Índia no Cenário Gastronômico: A Índia se destaca como o país com o maior número de restaurantes registrados, a maior quantidade de restaurantes 'gourmet', a maior diversidade de tipos de culinária, o maior número total de avaliações, e o maior número de restaurantes com entrega online e reservas. Isso a posiciona como um mercado extremamente vibrante e ativo para o Zomato.
   
2. Valor Agregado por Serviços Online e Reservas: Restaurantes que oferecem entrega online e aceitam reservas tendem a ter um desempenho superior. Aqueles com entrega online recebem, em média, significativamente mais avaliações, e os que aceitam reservas possuem um custo médio para duas pessoas consideravelmente mais alto, sugerindo que esses serviços são um diferencial para restaurantes de maior valor e popularidade.
   
3. Culinárias de Alto Custo: Certos tipos de culinária, como a 'Modern Australian', apresentam um valor médio de prato para duas pessoas excepcionalmente elevado. Isso indica a existência de um nicho de mercado para experiências gastronômicas de luxo e alto custo.
 
4. Variação Regional de Avaliações e Custos: Há uma grande disparidade na qualidade média e nos custos entre diferentes regiões. Por exemplo, enquanto a Austrália possui uma das maiores notas médias agregadas, o Brasil apresenta uma das menores. Da mesma forma, cidades como Pasay City têm o maior valor médio para um prato para dois, enquanto Gangtok possui a maior concentração de restaurantes com notas muito baixas (abaixo de 2.5).

5. Culinárias Altamente Avaliadas: A categoria de culinária 'Others' (Outros) possui a maior nota média agregada, o que pode indicar a popularidade de pratos menos convencionais ou altamente especializados. Além disso, culinárias específicas como Italiana e Americana abrigam vários restaurantes que alcançam a nota máxima (4.9), demonstrando excelência em diversas categorias.


# Conclusão

O objetivo primordial deste projeto foi transformar dados brutos em inteligência de negócios acionável. Através da criação de um conjunto de gráficos e tabelas estratégicas, conseguimos visualizar métricas cruciais sobre países, cidades, restaurantes e tipos de culinária. Essas análises não apenas revelam os pontos fortes e oportunidades em mercados existentes, como a dominância da Índia, mas também destacam o valor agregado por serviços como entrega online e reservas, bem como tendências de custos e avaliações que podem guiar futuras estratégias de expansão, otimização de serviços e identificação de nichos de alto valor.


## Visualize a análise completa

https://projetofomezerovictor.streamlit.app/

# Próximos passos

Verificar junto ao CEO dos dados que foram gerados quais são realmente essenciais e quais podem ser descartados para termos um dashboard mais limpo, tabalharia na melhora da identidade visual que não foi muito explorada nesse momento, e caso continuasse trabalhando em cima desses dados poderia realizar novas análises como:

1.Visualização Geoespacial de Restaurantes por Avaliação: Criar um mapa interativo utilizando Folium para visualizar a distribuição geográfica dos restaurantes, colorindo-os de acordo com sua aggregate_rating. Isso ajudará a identificar visualmente aglomerações de restaurantes bem avaliados e potenciais lacunas de mercado.

2.Análise de Popularidade e Desempenho de Culinárias por País: Investigar as culinárias mais populares e seu desempenho (média de avaliação, número de restaurantes) nos países com maior volume de dados (ex: Índia, EUA, Reino Unido). Apresentar esses dados em gráficos de barras agrupadas ou tabelas para o CEO.

3.Correlação entre Faixa de Preço e Avaliações/Votos: Analisar a relação entre a price_range (cheap, normal, expensive, gourmet) e as métricas de feedback do cliente (aggregate_rating e votes). Isso pode ser feito com gráficos de caixa ou barras para entender se restaurantes mais caros recebem mais votos ou melhores avaliações.

4.Impacto dos Serviços Online nos Restaurantes: Visualizar a diferença nas médias de avaliações, número de votos e custo médio para dois entre restaurantes que oferecem has_online_delivery e has_table_booking versus aqueles que não oferecem. Isso pode destacar o valor desses serviços.


