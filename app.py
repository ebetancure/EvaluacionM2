import pandas as pd
import streamlit as st


df = pd.read_csv('historico_resultados_pruebas_saber_11.csv')


df_año = df[(df['año_semestre'] == 20142) & (df['puntaje_global'] >= 300)]
df_matriculados = df[(df['matriculados'] >= 100)& (df['matriculados'] <= 110)] 
df_puntaje = df[df['puntaje_global'] >= 350]
df_establecimiento = df[df['establecimiento'] == 'col montessori']
df_comuna= df[(df['comuna'] == 'poblado') & ((df['año_semestre'] == 20152))]


st.title("Año semestre 2014-2 y puntaje global mayor que 300")
st.table(df_año)
st.title("Matriculados entre 100 y 110")
st.table(df_matriculados)
st.title("Puntaje mas de 350")
st.table(df_puntaje)
st.title("Establecimiento llamado col montessori")
st.table(df_establecimiento)
st.title("Comuna Poblado y año-semestre 2015-2")
st.table(df_comuna)
