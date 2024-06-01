import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Configurar a página do Streamlit
st.set_page_config(layout="wide")

# Carregar os dados de tickets
df = pd.read_csv("tickets.csv")

# Converter colunas de data e hora para o tipo datetime
df['DataAbertura'] = pd.to_datetime(df['DataAbertura'], format='%Y')
df['DataFechamento'] = pd.to_datetime(df['DataFechamento'], errors='coerce')
df['Ano'] = df['DataAbertura'].dt.year

# Sidebar para filtros
st.sidebar.title("Filtros")

# Opção para filtrar por funcionário ou ano
filtro_tipo = st.sidebar.selectbox("Filtrar por", ["Funcionário", "Ano"])

if filtro_tipo == "Funcionário":
    funcionarios = df['Funcionario'].unique()
    funcionario_selecionado = st.sidebar.selectbox("Escolha o funcionário", funcionarios)
    df_filtrado = df[df['Funcionario'] == funcionario_selecionado]
    
    # Calcular a quantidade de chamados atendidos por ano
    chamados_por_ano = df_filtrado[df_filtrado['Status'] == 'Concluido'].groupby('Ano').size().reset_index(name='ChamadosAtendidos')
    
      # Converter a coluna 'ChamadosAtendidos' para números inteiros
    chamados_por_ano['ChamadosAtendidos'] = chamados_por_ano['ChamadosAtendidos'].astype(int)
else:
    anos = df['Ano'].unique()
    ano_selecionado = st.sidebar.selectbox("Escolha o ano", anos)
    df_filtrado = df[df['Ano'] == ano_selecionado]
    
    # Calcular a quantidade de chamados atendidos por cada funcionário
    chamados_por_funcionario = df_filtrado[df_filtrado['Status'] == 'Concluido'].groupby('Funcionario').size().reset_index(name='ChamadosAtendidos')

# Calcular a quantidade de chamados feitos, concluídos e aguardando no filtro
total_chamados = len(df_filtrado)
concluidos = df_filtrado[df_filtrado['Status'] == 'Concluido'].shape[0]
aguardando = df_filtrado[df_filtrado['Status'] == 'Aguardando'].shape[0]

# Visualizar as informações
st.title("Dashboard de Atendimento de Tickets")

# Exibir as métricas principais
st.metric("Total de Chamados", total_chamados)
st.metric("Chamados Concluídos", concluidos)
st.metric("Chamados Aguardando", aguardando)

# Criar colunas para os gráficos
col1, col2 = st.columns(2)

# Gráfico de status dos chamados
fig_status = go.Figure(data=[go.Pie(
    labels=["Concluídos", "Aguardando"],
    values=[concluidos, aguardando],
    marker=dict(colors=["green", "c0c0c0"])  # Concluídos em verde, Aguardando em cinza
)])

col1.plotly_chart(fig_status, use_container_width=True)

# Gráfico de chamados por ano ou por funcionário, dependendo do filtro
if filtro_tipo == "Funcionário":
    fig_ano = px.bar(
        chamados_por_ano,
        x='Ano',
        y='ChamadosAtendidos',
        title=f"Chamados Atendidos por Ano ({funcionario_selecionado})",
        labels={'ChamadosAtendidos': 'Chamados Atendidos'},
    )
    
    # Definir formato dos números inteiros no eixo y
    fig_ano.update_layout(yaxis=dict(tickformat='d'))

    fig_ano.update_traces(marker_color='green')
    col2.plotly_chart(fig_ano, use_container_width=True)
else:
    fig_funcionario = px.bar(
        chamados_por_funcionario,
        x='Funcionario',
        y='ChamadosAtendidos',
        title=f"Chamados Atendidos por Funcionário ({ano_selecionado})",
        labels={'ChamadosAtendidos': 'Chamados Atendidos'},
    )
    fig_funcionario.update_traces(marker_color='green')
    col2.plotly_chart(fig_funcionario, use_container_width=True)