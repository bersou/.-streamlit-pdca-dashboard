
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Dashboard PDCA", layout="wide")

st.title("Dashboard Ciclo PDCA - Gestão à Vista")

df = pd.DataFrame({
    'Etapa': ['Planejar', 'Executar', 'Checar', 'Agir'],
    'Indicador': [85, 75, 90, 80]
})

col1, col2 = st.columns(2)
with col1:
    fig_bar = px.bar(df, x='Etapa', y='Indicador', color='Etapa',
                     title="Indicadores por Etapa do PDCA", text='Indicador')
    fig_bar.update_traces(textposition='outside')
    st.plotly_chart(fig_bar, use_container_width=True)

with col2:
    fig_pie = px.pie(df, values='Indicador', names='Etapa',
                     title="Distribuição dos Indicadores")
    st.plotly_chart(fig_pie, use_container_width=True)

st.markdown("### Detalhamento dos Indicadores")
st.dataframe(df)
