import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv')

st.header("Análisis de datos de venta de vehículos")

hist_button = st.button('Construir histograma')

if hist_button:
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    fig = px.histogram(car_data, x="odometer")

    st.plotly_chart(fig, use_container_width=True)

scatter_button = st.button('Construir gráfico de dispersión')

if scatter_button:
    st.write('Creación de un gráfico de dispersión para odómetro vs precio')

    fig = px.scatter(car_data, x="odometer", y="price")

    st.plotly_chart(fig, use_container_width=True)

    boxplot_button = st.button('Construir boxplot')

if boxplot_button:
    st.write('Creación de una boxplot para comparar precio vs condición del vehículo')
    fig_box = px.box(car_data, x="condition", y="price",
                     title="Precio por condición del vehículo")
    st.plotly_chart(fig_box, use_container_width=True)
