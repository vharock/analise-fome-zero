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

st.set_page_config(page_title='Home',page_icon='📊',layout='wide',initial_sidebar_state="expanded")


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

# Criando o mapa com os restaurantes agregados
def restaurantes_map(df1):
    grafico = df1.loc[:,['restaurant_name','average_cost_for_two','currency','aggregate_rating','country_code','city','cuisines','latitude','longitude']]
    map = folium.Map(location=[0, 0],zoom_start=2)
    marker_cluster = folium.plugins.MarkerCluster().add_to(map)
    for index,location in grafico.iterrows():
        folium.Marker([location['latitude'],location['longitude']],
                    popup=folium.Popup(f'''<h6><b>{location['restaurant_name']}</b></h6>
                    <h6>Preço: {location['average_cost_for_two']} ({location['currency']}) para dois <br>
                    Culinária: {location['cuisines']} <br>
                    Avaliação: {location['aggregate_rating']}/5.0</h6>''',
                    max_width=300,min_width=150),
                    tooltip=location["restaurant_name"],
                    icon=folium.Icon(color='green', icon='home', prefix='fa')).add_to(marker_cluster)

    folium_static(map,width=1024,height=600)




# Visão geral
#================================================
# BARRA LATERAL NO STREAMLIT
#================================================

image = Image.open('logo.png')
st.sidebar.image(image,width=350)

st.sidebar.markdown ( '---' )
st.sidebar.markdown ( '## Explore novos sabores' )
st.sidebar.markdown ( '---' )

st.write('# Fome Zero Dashboard!' )
st.write('### Seu guia definitivo para comer bem em qualquer lugar!' )

  


#================================================
# BARRA LATERAL NO STREAMLIT
#================================================

#Filtro de cidades

country = ['Philippines', 'Brazil', 'Australia', 'United States of America','Canada', 'Singapure', 'United Arab Emirates', 'India','Indonesia', 'New Zeland', 'England', 'Qatar', 'South Africa','Sri Lanka', 'Turkey']
country_options = st.sidebar.multiselect('Escolha os Países desejados',
                      country,
                      default=['Brazil','England','Qatar', 'South Africa','Canada','Australia'])


df1 = df1.loc[df1['country_code'].isin(country_options),:]

#================================================
# LAYOUT NO STREAMLIT
#================================================

st.markdown('---')


with st.container():
                
        col1,col2,col3,col4,col5 = st.columns(5,gap='large')
    
        with col1: 
            unique_restaurants = df1['restaurant_id'].nunique()
            col1.metric('Restaurantes Unicos',unique_restaurants)                  
                        
        with col2: 
            unique_countries = df1['country_code'].nunique()
            col2.metric('Países Unicos', unique_countries)           
            
                        
        with col3: 
            unique_cities = df1['city'].nunique()
            col3.metric('Cidades Unicas',unique_cities)
                       
        with col4: 
            total_ratings = df1['votes'].sum()
            total_ratings = f'{total_ratings:,.0f}'
            total_ratings = total_ratings.replace(',','.')
            col4.metric('Avaliações',total_ratings)

        with col5: 
            unique_cuisines = df1['cuisines'].nunique() 
            col5.metric('Tipos de Culinária',unique_cuisines)

            
st.markdown('---')           
with st.container():
        st.write('## Global Map')
        restaurantes_map(df1)



st.markdown('---')



# Não Apliquei função na limpeza do dataset para mostrar o raciocinio e a verificação da limpeza do dataset

'''
## Ask for help
        - @VictorAndrade
    '''





























