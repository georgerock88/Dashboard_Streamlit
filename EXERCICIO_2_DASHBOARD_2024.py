#!/usr/bin/env python
# coding: utf-8

# # Exercícios 
# 
# Utilize os arquivos do **RECLAME AQUI** e crie um dashboard com algumas caracteristicas. 
# 
# Empresas: 
# - Hapvida
# - Nagem
# - Ibyte
# 
# O painel deve conter tais informações: 
# 
# 1. Série temporal do número de reclamações. 
# 
# 2. Frequência de reclamações por estado. 
# 
# 3. Frequência de cada tipo de **STATUS**
# 
# 4. Distribuição do tamanho do texto (coluna **DESCRIÇÃO**) 
# 
# 
# Alguns botões devem ser implementados no painel para operar filtros dinâmicos. Alguns exemplos:: 
# 
# 1. Seletor da empresa para ser analisada. 
# 
# 2. Seletor do estado. 
# 
# 3. Seletor por **STATUS**
# 
# 4. Seletor de tamanho do texto 
# 
# Faça o deploy da aplicação. Dicas: 
# 
# https://www.youtube.com/watch?v=vw0I8i7QJRk&list=PLRFQn2r6xhgcDMhp9NCWMqDYGfeeYsn5m&index=16&t=252s
# 
# https://www.youtube.com/watch?v=HKoOBiAaHGg&t=515s
# 
# Exemplo do github
# https://github.com/jlb-gmail/streamlit_teste
# 
# 
# **OBSERVAÇÃO**
# 
# A resposta do exercicio é o link do github e o link da aplicação. Coloque-os abaixo.  
# 
# 
# 
# 

# In[1]:


import pandas as pd 


# In[3]:


path_ibyte = r"C:\Users\georg\OneDrive - GEORGE R BENTO\Cursos\MBA - Ciências de Dados\Dashboards Python\Exercício 2\RECLAMEAQUI_IBYTE.csv"
path_hapvida = r"C:\Users\georg\OneDrive - GEORGE R BENTO\Cursos\MBA - Ciências de Dados\Dashboards Python\Exercício 2\RECLAMEAQUI_HAPVIDA.csv"
path_nagem = r"C:\Users\georg\OneDrive - GEORGE R BENTO\Cursos\MBA - Ciências de Dados\Dashboards Python\Exercício 2\RECLAMEAQUI_NAGEM.csv"


# In[5]:


# Lendo o arquivo CSV
df_ibyte = pd.read_csv(path_ibyte)
df_hapvida = pd.read_csv(path_hapvida)
df_nagem = pd.read_csv(path_nagem)



# In[13]:


#Adicionando colunas com o nome da empresa
df_ibyte["EMPRESA"] = "Ibyte"
df_hapvida["EMPRESA"] = "Hapvida"
df_nagem["EMPRESA"] = "Nagem"


# In[14]:


# Concatenando os três DataFrames em um único DataFrame
df_unico = pd.concat([df_ibyte, df_hapvida, df_nagem], ignore_index=True)




# In[19]:


# Exibindo o resultado
df_unico.head()


# In[21]:


print(df_unico.columns)


# 1. Análise de Serie temporal
# 

# In[23]:


import matplotlib.pyplot as plt
import pandas as pd

# Converter as colunas de 'ANO', 'MES' e 'DIA' em um datetime
df_unico['DATA'] = pd.to_datetime(df_unico[['ANO', 'MES', 'DIA']].rename(columns={'ANO': 'year', 'MES': 'month', 'DIA': 'day'}))

# Agrupar por data e contar o número de reclamações por dia
serie_temporal = df_unico.groupby('DATA').size()

# Plotar a série temporal
plt.figure(figsize=(12, 6))
serie_temporal.plot()
plt.title('Série Temporal do Número de Reclamações')
plt.xlabel('Data')
plt.ylabel('Número de Reclamações')
plt.show()



# 2. Frequencia por estado

# In[24]:


# Agrupar por 'LOCAL' e contar o número de reclamações
frequencia_por_estado = df_unico['LOCAL'].value_counts()

# Exibir a distribuição
print(frequencia_por_estado)


# 3. Frequencia de cada tipo de estado

# In[25]:


# Agrupar por 'STATUS' e contar o número de ocorrências
frequencia_por_status = df_unico['STATUS'].value_counts()

# Exibir a distribuição
print(frequencia_por_status)


# 4. Distribuição do tamanho do texto (coluna DESCRIÇÃO)

# In[26]:


# Calcular o tamanho do texto em cada linha da coluna 'DESCRICAO'
df_unico['TAMANHO_DESCRICAO'] = df_unico['DESCRICAO'].apply(len)

# Plotar o histograma do tamanho das descrições
plt.figure(figsize=(12, 6))
df_unico['TAMANHO_DESCRICAO'].hist(bins=30)
plt.title('Distribuição do Tamanho das Descrições')
plt.xlabel('Tamanho do Texto')
plt.ylabel('Frequência')
plt.show()


# CRIANDO O PAINEL NO STREAMLIT

import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd





# In[27]:


import streamlit as st 


# In[28]:



import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

st.title("TRABALHO DA DISCIPLINA - DASHBOARDS BIBLIOTECAS R/PYTHON")
st.header("MBA em Ciência de Dados - Turma 07")
st.subheader("Objetivo: Analisar registros de reclamações das empresas: Ibyte, Hapvida e Nagem.")
st.subheader("Source: Base de dados do Site Reclame Aqui.")
st.subheader("Professor: Jorge Luiz")
st.subheader("Aluno: George Rodrigues Bento")
print("")

empresas = df_unico['EMPRESA'].unique()

# Dicionário de logos 
logos = {
    'Ibyte': r"C:\Users\georg\OneDrive - GEORGE R BENTO\Cursos\MBA - Ciências de Dados\Dashboards Python\Exercício 2\imagens\logo_ibyte.png",
    'Hapvida': r"C:\Users\georg\OneDrive - GEORGE R BENTO\Cursos\MBA - Ciências de Dados\Dashboards Python\Exercício 2\imagens\logo_hapvida.png",
    'Nagem': r"C:\Users\georg\OneDrive - GEORGE R BENTO\Cursos\MBA - Ciências de Dados\Dashboards Python\Exercício 2\imagens\logo_nagem.png",
   
    
}

# Menu lateral
st.sidebar.title('Menu')
paginaSelecionada = st.sidebar.selectbox('Selecione a análise', [
    '1. Série temporal do número de reclamações.',
    '2. Frequência de reclamações por estado.',
    '3. Frequência de cada tipo de **STATUS**',
    '4. Distribuição do tamanho do texto (coluna **DESCRIÇÃO**)'
], key='pagina_selecionada')  # Chave exclusiva para a seleção da página

# Widget de seleção para escolher a empresa
empresa_selecionada = st.sidebar.selectbox("Selecione a Empresa", empresas, key='empresa_selecionada')  # Chave exclusiva para a seleção da empresa

# Filtrar o DataFrame com base na empresa selecionada
df_filtrado = df_unico[df_unico['EMPRESA'] == empresa_selecionada]

# Exibir a logo da empresa selecionada
if empresa_selecionada in logos:
    st.image(logos[empresa_selecionada], caption=f'Empresa {empresa_selecionada}', width=100)  # Ajustando a largura da logo
    

# Análises com base na página selecionada
if paginaSelecionada == '1. Série temporal do número de reclamações.':
    st.title('Série temporal do número de reclamações')
    
    # Converter as colunas de 'ANO', 'MES' e 'DIA' em um datetime
    df_filtrado['DATA'] = pd.to_datetime(df_filtrado[['ANO', 'MES', 'DIA']].rename(columns={'ANO': 'year', 'MES': 'month', 'DIA': 'day'}))
    
    # Agrupar por data e contar o número de reclamações por dia
    serie_temporal = df_filtrado.groupby('DATA').size()
    
    # Plotar a série temporal
    plt.figure(figsize=(12, 6))
    serie_temporal.plot()
    plt.title(f'Série Temporal do Número de Reclamações - {empresa_selecionada}')
    plt.xlabel('Data')
    plt.ylabel('Número de Reclamações')
    st.pyplot(plt)
    plt.clf()  # Limpar a figura

elif paginaSelecionada == '2. Frequência de reclamações por estado.':
    st.title('Frequência de reclamações por estado')
    
    # Agrupar por 'LOCAL' e contar o número de reclamações
    frequencia_por_estado = df_filtrado['LOCAL'].value_counts()
    
    # Exibir a distribuição
    st.bar_chart(frequencia_por_estado)  # Exibir gráfico de barras com a frequência por estado
    st.table(frequencia_por_estado)  # Tabela de frequências

elif paginaSelecionada == '3. Frequência de cada tipo de **STATUS**':
    st.title('Frequência de cada tipo de **STATUS**')
    
    # Agrupar por 'STATUS' e contar o número de ocorrências
    frequencia_por_status = df_filtrado['STATUS'].value_counts()
    
    # Exibir a distribuição
    st.bar_chart(frequencia_por_status)  # Exibir gráfico de barras com a frequência por status
    st.table(frequencia_por_status)  # Tabela de frequências

elif paginaSelecionada == '4. Distribuição do tamanho do texto (coluna **DESCRIÇÃO**)':
    st.title('Distribuição do tamanho do texto (coluna **DESCRIÇÃO**)')
    
    # Calcular o tamanho do texto em cada linha da coluna 'DESCRICAO'
    df_filtrado['TAMANHO_DESCRICAO'] = df_filtrado['DESCRICAO'].apply(len)
    
    # Plotar o histograma do tamanho das descrições
    plt.figure(figsize=(12, 6))
    df_filtrado['TAMANHO_DESCRICAO'].hist(bins=30)
    plt.title(f'Distribuição do Tamanho das Descrições para {empresa_selecionada}')
    plt.xlabel('Tamanho do Texto')
    plt.ylabel('Frequência')
    
    # Exibir o gráfico no Streamlit
    st.pyplot(plt)
    plt.clf()  # Limpar a figura
