import pandas as pd
import plotly.express as px
import streamlit as st

# Lendo o dataset a partir de uma URL e armazenando-o em um DataFrame chamado 'df'
df = pd.read_csv('https://raw.githubusercontent.com/wcota/covid19br/master/cases-brazil-states.csv')

# Melhorando o nome das colunas do DataFrame
df = df.rename(columns={'newDeaths': 'Novos óbitos',
                        'newCases': 'Novos casos',
                        'deaths_per_100k_inhabitants': 'Óbitos por 100 mil habitantes',
                        'totalCases_per_100k_inhabitants': 'Casos por 100 mil habitantes'})

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

# Criando um gráfico de linha usando o Plotly Express com base nos dados do estado selecionado
fig = px.line(df_state, x="date", y=column, title=column + " - " + state)
fig.update_layout(xaxis_title='Data', yaxis_title=column.upper(), title={'x': 0.5})

# Adicionando um título à página da aplicação
st.title('DADOS COVID - BRASIL')

# Escrevendo uma descrição na página da aplicação
st.write('Nessa aplicação, o usuário tem a opção de escolher o estado e o tipo de informação para mostrar')

# Renderizando o gráfico criado na página da aplicação
st.plotly_chart(fig, use_container_width=True)
