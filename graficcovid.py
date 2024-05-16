import pandas as pd
import altair as alt
import streamlit as st

# Lendo o dataset a partir de uma URL e armazenando-o em um DataFrame chamado 'df'
df = pd.read_csv('https://raw.githubusercontent.com/wcota/covid19br/master/cases-brazil-states.csv')

# Melhorando o nome das colunas do DataFrame
df = df.rename(columns={'newDeaths': 'Novos óbitos',
                        'newCases': 'Novos casos',
                        'deaths_per_100k_inhabitants': 'Óbitos por 100 mil habitantes',
                        'totalCases_per_100k_inhabitants': 'Casos por 100 mil habitantes'})

# Adicionando um título e um subtítulo à página da aplicação
st.title('Análise de casos de COVID-19 no Brasil')
st.write('Esta aplicação permite visualizar dados sobre casos de COVID-19 no Brasil.')

# Obtendo a lista de estados presentes no DataFrame
estados = list(df['state'].unique())

# Criando um seletor de estado na barra lateral da aplicação
state = st.sidebar.selectbox('Qual estado? ', estados)

# Definindo as opções para seleção de coluna
colunas = ['Novos óbitos', 'Novos casos', 'Óbitos por 100 mil habitantes', 'Casos por 100 mil habitantes']

# Criando um seletor de coluna na barra lateral da aplicação
column = st.sidebar.selectbox('Qual tipo de informação? ', colunas)

# Filtrando as linhas do DataFrame que correspondem ao estado selecionado
df_state = df[df['state'] == state]

# Criando um gráfico de linha usando o Altair com base nos dados do estado selecionado
chart = alt.Chart(df_state).mark_line().encode(
    x='date:T',
    y=column,
    tooltip=[column, 'date']
).properties(
    width=700,
    height=400
).configure_axis(
    labelFontSize=12,
    titleFontSize=14
).configure_title(
    fontSize=16
).configure_legend(
    labelFontSize=12,
    titleFontSize=14
)

# Adicionando um título acima do gráfico
st.header('Gráfico COVID-19 no Brasil')

# Exibindo o gráfico
st.altair_chart(chart, use_container_width=True)
