import pandas as pd
import inflection
import folium
import streamlit as st
import plotly.express  as px
import plotly.graph_objects as go
from haversine import haversine
from PIL import Image
from streamlit_folium import folium_static
from streamlit_folium import st_folium


st.set_page_config(
    page_title='Cuisines', page_icon='🍽️', layout='wide')


df= pd.read_csv("dataset/zomato.csv")
df1= df.copy()

# ( FUNÇÕES )
# Para colocar o nome dos países com base no código de cada país
COUNTRIES = {
1: "India",
14: "Australia",
30: "Brazil",
37: "Canada",
94: "Indonesia",
148: "New Zeland",
162: "Philippines",
166: "Qatar",
184: "Singapure",
189: "South Africa",
191: "Sri Lanka",
208: "Turkey",
214: "United Arab Emirates",
215: "England",
216: "United States of America",
}
def country_name(country_id):
  return COUNTRIES[country_id]
      
df1['Country Code'] = df1.loc[:, 'Country Code'].apply(lambda x: country_name(x))

# Criar a categoria do tipo de comida com base no range de valores
def create_price_tye(price_range):
  if price_range == 1:
    return "cheap"
  elif price_range == 2:
    return "normal"
  elif price_range == 3:
    return "expensive"
  else:
    return "gourmet"
    
df1['Price range'] = df1.loc[:, 'Price range'].apply(lambda x: create_price_tye(x))

# Criar o nome das cores com base nos códigos de cores
COLORS = {
"3F7E00": "darkgreen",
"5BA829": "green",
"9ACD32": "lightgreen",
"CDD614": "orange",
"FFBA00": "red",
"CBCBC8": "darkred",
"FF7800": "darkred",
}
def color_name(color_code):
  return COLORS[color_code]
  
df1['Expressed color'] = df1.loc[:, 'Rating color'].apply(lambda x: color_name(x))

# Renomear as colunas do DataFrame
def rename_columns(dataframe):
    df = dataframe.copy()
    title = lambda x: inflection.titleize(x)
    snakecase = lambda x: inflection.underscore(x)
    spaces = lambda x: x.replace(" ", "")
    cols_old = list(df.columns)
    cols_old = list(map(title, cols_old))
    cols_old = list(map(spaces, cols_old))
    cols_new = list(map(snakecase, cols_old))
    df.columns = cols_new
    return df

df1 = rename_columns(df1)

# (LIMPEZA DO DATASET)
# Verificando dados faltantes por coluna
missing_data_per_column = df1.isnull().sum()
print("Dados faltantes por coluna:")
print(missing_data_per_column)

# Verificando o total de dados faltantes no DataFrame
total_missing_data = df1.isnull().sum().sum()
print(f"\nTotal de dados faltantes no DataFrame: {total_missing_data}")

# Removendo a coluna 'Switch to order menu' pois não possui valores
df1 = df1.drop(labels=['switch_to_order_menu'], axis='columns')

#Categorizar todos os restaurantes somente por um tipo de culinária
df1['cuisines'] = df1['cuisines'].astype(str)
df1["cuisines"] = df1.loc[:, "cuisines"].apply(lambda x: x.split(",")[0])

# Removendo os NaN da coluna Cuisines 
df1 = df1.loc[(df1['cuisines'] != 'nan'),:].copy()
df1 = df1.loc[(df1['cuisines'] != 'Drinks Only'),:].copy()
df1 = df1.loc[(df1['cuisines'] != 'Mineira'),:].copy()

# Removendo linhas duplicadas do DataFrame
df1 = df1.drop_duplicates().reset_index(drop=True)

# Confirmação se os dados foram limpos
missing_data_per_column = df1.isnull().sum()
print("Dados faltantes por coluna:")
print(missing_data_per_column)

total_missing_data = df1.isnull().sum().sum()
print(f"\nTotal de dados faltantes no DataFrame: {total_missing_data}")

def max_rating_cuisines(df1, tipo):
    # 1. Filtra pela culinária e ordena por Nota (DESC) e ID (ASC) como critério de desempate
    # Fazemos tudo em uma única passagem
    restaurante = (df1.loc[df1['cuisines'] == tipo, :]
                      .sort_values(['aggregate_rating', 'restaurant_id'], 
                                   ascending=[False, True])
                      .iloc[0]) # Pega o melhor (primeira linha)

    # 2. Montagem das strings usando os nomes das colunas (mais seguro que índices numéricos)
    label = f"{restaurante['cuisines']}: {restaurante['restaurant_name']}"
    value = f"{restaurante['aggregate_rating']}/5.0"
    
    ajuda = (f"País: {restaurante['country_code']}\n\n"
             f"Cidade: {restaurante['city']}\n\n"
             f"Média Prato para dois: {restaurante['average_cost_for_two']} {restaurante['currency']}")
    
    return label, value, ajuda


#================================================
# BARRA LATERAL NO STREAMLIT
#================================================
#Filtro de cidades
country = ['Philippines', 'Brazil', 'Australia', 'United States of America','Canada', 'Singapure', 'United Arab Emirates', 'India','Indonesia', 'New Zeland', 'England', 'Qatar', 'South Africa','Sri Lanka', 'Turkey']
country_options = st.sidebar.multiselect('Escolha os Países desejados',
                      country,
                      default=['Brazil','England','Qatar', 'South Africa','Canada','Australia'])

# Aplicando o filtro de cidades
df1 = df1.loc[df1['country_code'].isin(country_options),:]

# Filtro slider para quantidade de restaurantes
num_restaurants = st.sidebar.slider(
    'Selecione a Quantidade de Restaurantes',
    1, 20, 10 # Min, Max, Valor Inicial
)

# Filtro de tipos de culinária
cuisines = df1['cuisines'].unique().tolist()
cuisine_options = st.sidebar.multiselect('Escolha os Tipos de Culinária', cuisines, default=['BBQ','Japanese', 'Brazilian','Arabian','American','Italian'])

# Aplicando o filtro de culinária
df1 = df1.loc[df1['cuisines'].isin(cuisine_options), :]



#================================================
# LAYOUT NO STREAMLIT
#================================================

st.title("Visão Tipos de Culinária 🍽️")
with st.container():
        st.markdown('''___''')
        st.header('Melhores Restaurantes dos Principais tipos Culinários')
    
with st.container():
               
        col1,col2,col3,col4,col5 = st.columns(5,gap='large')
        with col1:             
            label, value, ajuda = max_rating_cuisines(df1,'Brazilian')
            col1.metric(label,value,help=ajuda)
                        
        with col2:
            label, value, ajuda = max_rating_cuisines(df1,'Japanese')
            col2.metric(label,value,help=ajuda)
                          
                
        with col3:
            label, value, ajuda = max_rating_cuisines(df1,'Arabian')
            col3.metric(label,value,help=ajuda)
                
                            
        with col4:
            label, value, ajuda = max_rating_cuisines(df1,'American')
            col4.metric(label,value,help=ajuda)
            
        with col5:
            label, value, ajuda = max_rating_cuisines(df1,'Italian')
            col5.metric(label,value,help=ajuda)



            
with st.container(): 
    st.markdown('''___''')


# Obtendo os restaurantes mais bem avaliados (usando aggregate_rating e votos como desempate)
top_restaurants_df = df1.sort_values(by=['aggregate_rating', 'votes'], ascending=[False, False]).head(num_restaurants)

st.subheader(f'Top {num_restaurants} Restaurantes Mais Bem Avaliados:')
st.dataframe(top_restaurants_df[['restaurant_name', 'country_code', 'city', 'cuisines', 'average_cost_for_two', 'currency', 'aggregate_rating', 'votes']])


             
            
            

with st.container(): 
    st.markdown('''___''')
    
    col1, col2 = st.columns(2)
        
    with col1:
        
        # Agrupando por culinária e calculando a média da nota agregada
        average_rating_per_cuisine = df1.groupby('cuisines')['aggregate_rating'].mean().reset_index()
        
        # Ordenando e selecionando os top 10
        top_10_cuisines = average_rating_per_cuisine.sort_values(by='aggregate_rating', ascending=False).head(num_restaurants)
    
        fig = px.bar(
            top_10_cuisines,
            x='cuisines',
            y='aggregate_rating',
            title=(f'Top {num_restaurants} Melhores Tipos de Culinárias (Média de Avaliação):'),
            labels={'cuisines': 'Tipo de Culinária', 'aggregate_rating': 'Média de Avaliação'},
            text='aggregate_rating',
            color='cuisines'
    )
        fig.update_traces(texttemplate='%{text:.2f}', textposition='outside')
        fig.update_layout(xaxis_tickangle=-45)
        st.plotly_chart(fig)


    with col2:
        
        # Gráfico Top 10 Piores Tipos de Culinárias por Média de Avaliação
        
        # Agrupando por culinária e calculando a média da nota agregada
        average_rating_per_cuisine = df1.groupby('cuisines')['aggregate_rating'].mean().reset_index()
        
        # Ordenando e selecionando os top 10 piores (menores notas)
        top_10_worst_cuisines = average_rating_per_cuisine.sort_values(by='aggregate_rating', ascending=True).head(num_restaurants)
        
        fig = px.bar(
            top_10_worst_cuisines,
            x='cuisines',
            y='aggregate_rating',
            title=(f'Top {num_restaurants} Piores Tipos de Culinárias (Média de Avaliação):'),
            labels={'cuisines': 'Tipo de Culinária', 'aggregate_rating': 'Média de Avaliação'},
            text='aggregate_rating',
            color='cuisines'
        )
        fig.update_traces(texttemplate='%{text:.2f}', textposition='outside')
        fig.update_layout(xaxis_tickangle=-45)
        st.plotly_chart(fig)




                 




               