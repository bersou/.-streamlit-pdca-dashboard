import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Dashboard PDCA", layout="wide")

st.title("Dashboard Ciclo PDCA - Gestão à Vista")

# Dados atualizados
data = {
    'Linhas': ['MDF 1', 'MDF 1', 'MDF 2', 'MDF 2'],
    'Turno': ['B', 'B', 'B', 'B'],
    'Umidade %': [42.00, 47.90, 62.03, 61.98],
    'Densidade': [219.11, 240.22, 258.08, 307.40],
    'Classificação Total (g)': [116.36, 104.19, 161.49, 145.57],
}

df = pd.DataFrame(data)

# Configuração das colunas para exibição
col1, col2 = st.columns(2)

# Gráfico de linhas para densidade
with col1:
    fig_line = px.line(df, x='Linhas', y='Densidade', color='Turno',
                       markers=True,
                       title="Densidade por Linha e Turno")
    fig_line.update_traces(line=dict(width=3), marker=dict(size=10))
    fig_line.update_layout(title_font_size=16, legend_title="Turno")
    st.plotly_chart(fig_line, use_container_width=True)

# Gráfico de barras empilhadas para classificação total
with col2:
    fig_bar = px.bar(df, x='Linhas', y='Classificação Total (g)', color='Turno',
                     title="Classificação Total por Linha e Turno")
    fig_bar.update_traces(texttemplate='%{y:.2f}', textposition='outside')
    fig_bar.update_layout(title_font_size=16, legend_title="Turno")
    st.plotly_chart(fig_bar, use_container_width=True)

# Adicionando um gráfico de dispersão para Umidade % vs Densidade
st.markdown("### Relação entre Umidade e Densidade")
fig_scatter = px.scatter(df, x='Umidade %', y='Densidade', color='Linhas',
                         size='Classificação Total (g)', hover_name='Turno',
                         title="Relação entre Umidade e Densidade")
fig_scatter.update_layout(title_font_size=16, legend_title="Linhas")
st.plotly_chart(fig_scatter, use_container_width=True)

# Exibição detalhada dos dados
st.markdown("### Detalhamento dos Dados")
st.dataframe(df)