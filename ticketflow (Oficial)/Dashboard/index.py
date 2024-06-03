import psycopg2
import pandas as pd
import plotly.express as px
import streamlit as st
from datetime import datetime

# Configurar a largura da página para wide
st.set_page_config(layout="wide")

# Estabelecer conexão com o banco de dados
def get_db_connection():
    conn = psycopg2.connect(
        dbname="OG1 System",
        user="postgres",
        password="postgres",
        host="localhost"
    )
    return conn

# Função para buscar os dados da tabela cadsolicitacao
def fetch_data():
    conn = get_db_connection()
    query = "SELECT * FROM cadsolicitacao"
    df = pd.read_sql(query, conn)
    conn.close()
    return df

# Função para buscar os dados da tabela cadparceiro
def fetch_parceiros():
    conn = get_db_connection()
    query_parceiros = "SELECT codigoparceiro, a_descricao FROM cadparceiro"
    df_parceiros = pd.read_sql(query_parceiros, conn)
    conn.close()
    return df_parceiros

# Função principal do Streamlit
def main():
    st.title("Dashboard de Solicitações")

    # Mostrar estatísticas gerais
    df = fetch_data()
    total_solicitacoes = len(df)
    solicitacoes_andamento = len(df[df['situacao'] == 'Em andamento'])
    solicitacoes_aberto = len(df[df['situacao'] == 'Aberto'])

    st.markdown(f"**Total de Solicitações:** {total_solicitacoes}")
    st.markdown(f"**Solicitações em Andamento:** {solicitacoes_andamento}")
    st.markdown(f"**Solicitações em Aberto:** {solicitacoes_aberto}")

    # Sidebar para filtros
    st.sidebar.header("Filtros")
    
    # Filtro de data
    start_date = st.sidebar.date_input("Data Inicial", datetime(2024, 5, 1))
    end_date = st.sidebar.date_input("Data Final", datetime.today())
    
    # Seleção de empresa
    df_parceiros = fetch_parceiros()
    selected_partner = st.sidebar.selectbox("Selecione a Empresa", ["Todas"] + df_parceiros['a_descricao'].tolist())

    # Variável para rastrear se os filtros foram restaurados
    filtros_restaurados = False

    # Opção para restaurar os filtros
    if st.sidebar.button("Voltar ao Início"):
        start_date = datetime(2024, 5, 1)
        end_date = datetime.today()
        selected_partner = "Todas"
        filtros_restaurados = True

    # Buscar os dados
    df = fetch_data()
    
    # Filtrar por data
    df['data'] = pd.to_datetime(df['data'])
    df = df[(df['data'] >= pd.to_datetime(start_date)) & (df['data'] <= pd.to_datetime(end_date))]

    # Filtrar por parceiro
    if selected_partner != "Todas":
        partner_code = df_parceiros[df_parceiros['a_descricao'] == selected_partner]['codigoparceiro'].values[0]
        df = df[df['codigoparceiro'] == partner_code]

    # Definir as cores para cada situação
    cores = {'Aberto': '#F44E3F', 'Fechado': '#229A00', 'Em andamento': '#87CEFA'}

    # Dividir os gráficos em duas colunas
    col1, col2 = st.columns(2)

    # Gráfico de Pizza para a coluna 'situacao'
    with col1:
        if selected_partner == "Todas":
            fig_pizza = px.pie(df, names='situacao', color='situacao', color_discrete_map=cores, title='Distribuição das Situações das Solicitações')
        else:
            fig_pizza = px.pie(df, names='situacao', color='situacao', color_discrete_map=cores, title=f'Distribuição das Situações das Solicitações - {selected_partner}')
        st.plotly_chart(fig_pizza, use_container_width=True)

    # Mostrar o gráfico de quantidade de chamados por empresa apenas na página inicial e na de restaurar filtros
    if selected_partner == "Todas" or filtros_restaurados:
        with col2:
            df_merged = df.merge(df_parceiros, left_on='codigoparceiro', right_on='codigoparceiro')
            solicitacoes_por_parceiro = df_merged['a_descricao'].value_counts().reset_index()
            solicitacoes_por_parceiro.columns = ['Empresa', 'Chamados']
            st.plotly_chart(px.bar(solicitacoes_por_parceiro, x='Chamados', y='Empresa', title='Quantidade de Solicitações por Parceiro', orientation='h'), use_container_width=True)

    # Mostrar detalhes dos chamados filtrados, se um parceiro específico for selecionado
    if selected_partner != "Todas":
        st.header("Detalhes dos Chamados")
        df_filtered = df[['descricao', 'situacaosuporte', 'correcaosuporte']]
        st.write(df_filtered)

if __name__ == "__main__":
    main()
