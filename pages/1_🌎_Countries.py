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
    page_title='Countries', page_icon='🌎', layout='wide')


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
df1 = df1.dropna(subset=['cuisines'])
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


#================================================
# BARRA LATERAL NO STREAMLIT
#================================================
country = ['Philippines', 'Brazil', 'Australia', 'United States of America','Canada', 'Singapure', 'United Arab Emirates', 'India','Indonesia', 'New Zeland', 'England', 'Qatar', 'South Africa','Sri Lanka', 'Turkey']
country_options = st.sidebar.multiselect('Escolha os Países desejados',
                      country,
                      default=['Brazil','England','Qatar', 'South Africa','Canada','Australia'])

#Filtro de cidades
df1 = df1.loc[df1['country_code'].isin(country_options),:]

#================================================
# LAYOUT NO STREAMLIT
#================================================

st.title("Visão Países :earth_americas:")

with st.container():
        st.markdown('''___''')
        st.header('Quantidade de Restaurantes registrados por País')
restaurants_per_country_df = df1.groupby('country_code')['restaurant_id'].nunique().reset_index()
restaurants_per_country_df.columns = ['country_code', 'restaurant_count']
restaurants_per_country_df = restaurants_per_country_df.sort_values(by='restaurant_count', ascending=False)

fig = px.bar(
    restaurants_per_country_df,
    x='country_code',
    y='restaurant_count',
    labels={'country_code': 'País', 'restaurant_count': 'Número de Restaurantes'},
    text='restaurant_count',
    color='country_code'
)
st.plotly_chart(fig)
               
                 

with st.container(): 
        st.markdown('''___''')
        st.header('Quantidade de Cidades registradas por País')
               
cities_per_country_df = df1.groupby('country_code')['city'].nunique().reset_index()
cities_per_country_df.columns = ['country_code', 'city_count']
cities_per_country_df = cities_per_country_df.sort_values(by='city_count', ascending=False)

fig = px.bar(
    cities_per_country_df,
    x='country_code',
    y='city_count',
    labels={'country_code': 'País', 'city_count': 'Número de Cidades'},
    text='city_count',
    color='country_code'
)
st.plotly_chart(fig)

                          
with st.container(): 
    st.markdown('''___''')
    
    col1, col2 = st.columns(2)
        
    with col1:
        st.markdown('##### Média de avaliações feitas por País')
    
        average_ratings_per_country_df = round(df1.groupby('country_code')['votes'].mean().reset_index(),2)
        average_ratings_per_country_df.columns = ['country_code','average_votes']
        average_ratings_per_country_df = average_ratings_per_country_df.sort_values(by='average_votes', ascending=False)
        
        fig = px.bar(average_ratings_per_country_df,
            x='country_code',
            y='average_votes',
            labels={'country_code': 'País','average_votes': 'Média de Avaliação'},
            text='average_votes',
            color='country_code'
        )

        st.plotly_chart(fig)

    with col2:
        st.markdown('##### Média de preço de um prato para duas pessoas por País')
        
        average_cost_for_two_per_country_df = round(df1.groupby('country_code')['average_cost_for_two'].mean().reset_index(),2)
        average_cost_for_two_per_country_df.columns = ['country_code', 'average_cost_for_two']
        average_cost_for_two_per_country_df = average_cost_for_two_per_country_df.sort_values(by='average_cost_for_two', ascending=False)

        fig = px.bar(
            average_cost_for_two_per_country_df,
            x='country_code',
            y='average_cost_for_two',
            labels={'country_code': 'País', 'average_cost_for_two': 'Média de Custo'},
            text='average_cost_for_two',
            color='country_code'
        )
        st.plotly_chart(fig)
            
            


